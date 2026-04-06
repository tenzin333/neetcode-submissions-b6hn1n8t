class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board =  [["."] * n for _ in range(n)]
        cols = set()
        diag = set()    # row - col
        antidiag = set() # row + col

        res = []

        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in  board ])
                return
            

            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in antidiag:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diag.add(row-col)
                antidiag.add(row+col)

                dfs(row+1)

                board[row][col] = '.'
                cols.remove(col)
                diag.remove(row-col)
                antidiag.remove(row+col)

        dfs(0)

        return res