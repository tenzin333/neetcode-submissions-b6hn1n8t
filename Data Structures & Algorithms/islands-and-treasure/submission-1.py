class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid), len(grid[0])

        visited = set()

        q = collections.deque()

        def addRow(r,c):
            if r < 0 or c<0 or r>=rows or c>=cols or grid[r][c] == -1 or (r,c) in visited :
                return 
            
            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                        q.append([r,c])
                        visited.add((r,c))
        

        dist = 0

        while q:
            for i in range(len(q)):   # [(g1) , (g2) ...]
                r, c = q.popleft()

                grid[r][c] = dist

                addRow(r+1,c)
                addRow(r-1,c)
                addRow(r,c-1)
                addRow(r,c+1)
            dist += 1
