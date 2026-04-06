class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        fresh = 0

        def addRow(r, c):
            nonlocal fresh   # ✅ needed
            
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] != 1 or
                (r, c) in visited
            ):
                return 
            
            q.append((r, c))
            visited.add((r, c))
            grid[r][c] = 2     # ✅ convert to rotten
            fresh -= 1         # ✅ correct place

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                addRow(r - 1, c)
                addRow(r + 1, c)
                addRow(r, c - 1)
                addRow(r, c + 1)

            time += 1

        return time if fresh == 0 else -1