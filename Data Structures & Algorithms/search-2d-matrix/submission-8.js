class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const Rows =  matrix.length;
        const Cols = matrix[0].length;

        let top = 0;
        let bot = Rows-1;
        let row = null;
        //finding the correct row
        while(top<=bot) {
            row= top + Math.floor((bot-top)/2); 
            if(target > matrix[row][Cols-1]){
                top = row+1;
            }else if(target < matrix[row][0]){
                bot = row-1;
            }else{
                break; // candidate row
            }
        }

        if(top>bot) return false;

        let l = 0;
        let r = Cols-1;
        while(l<=r){
            const mid = l+ Math.floor((r-l)/2);
            if(target == matrix[row][mid]){
                return true;
            }else if(target < matrix[row][mid]){
                r = mid-1;
            }else{
                l = mid+1;
            }

        }
        return false;

    }
}
