
let row = 9
let col = 9

class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let seen = new Set();

        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                let digit = board[i][j];
                if (digit === '.') continue;

                // Create unique keys for each constraint
                let rowKey = `row ${i} has ${digit}`;
                let colKey = `col ${j} has ${digit}`;
                let boxKey = `box ${Math.floor(i / 3) * 3 + Math.floor(j / 3)} has ${digit}`;

                if (seen.has(rowKey) || seen.has(colKey) || seen.has(boxKey)) {
                    return false;
                }

                seen.add(rowKey);
                seen.add(colKey);
                seen.add(boxKey);
            }
        }
        return true;
    }
}
