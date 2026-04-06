
let row = 9
let col = 9

class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {

        let boxSet = Array.from({length: row}, () => new Set())
        let colsSet = Array.from({length: row} , () =>  new Set())
        let rowsSet = Array.from({length: row} , () =>  new Set())

        for(let i=0;i<9;i++){
            for(let j=0;j<9;j++){
                let digit = board[i][j]

                if(digit=='.') continue;
                let boxIndex = Math.floor(i/3) * 3 + Math.floor(j/3)
                
                if(rowsSet[i].has(digit) || 
                 colsSet[j].has(digit) ||
                 boxSet[boxIndex].has(digit)
                ){
                    return false
                }

                rowsSet[i].add(digit)
                colsSet[j].add(digit)
               
                boxSet[boxIndex].add(digit)
            }
        }
        return true
    }
}
