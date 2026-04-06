class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        fresh = 0
        time = 0

        rows , cols = len(grid), len(grid[0])

        def addRow(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>= rows or c>=cols or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append([r,c])
            fresh -=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        
       
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                addRow(r+1,c)
                addRow(r-1,c)
                addRow(r,c+1)
                addRow(r,c-1)
                
            time += 1
        return time if fresh == 0 else -1
