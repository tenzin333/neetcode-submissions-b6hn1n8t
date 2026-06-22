

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        ROWS , COLS = len(board), len(board[0])

        
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        # {
        #     0: [1,2,3,4,5,6]
        # }


        for row in range(ROWS):
            for col in range(COLS):
                val = board[row][col]

                if val == '.':
                    continue
                if val in rowSet[row] or val in colSet[col] or val in boxSet[(row//3, col//3)]:
                    return False
            
                colSet[col].add(val)
                rowSet[row].add(val)
                boxSet[row//3, col//3].add(val)
                
        return True
