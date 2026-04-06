class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows , cols = len(board), len(board[0])

        q = collections.deque()
        
        def bfs(r,c):
            if r<0 or c<0 or r>= rows or c>=cols or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            q.append([r,c])


            
        for r in range(rows):
            bfs(r,0)
            bfs(r,cols-1)

        for c in range(cols):
            bfs(0,c)
            bfs(rows-1, c)

        
        while q:
            for  _ in range(len(q)):
                r , c = q.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'


