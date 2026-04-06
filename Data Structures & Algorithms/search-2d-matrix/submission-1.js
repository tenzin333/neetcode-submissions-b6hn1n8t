class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const m = matrix.length;
        const n = matrix[0].length;
        for(let i=0;i<m;i++){
            for(let j=0;j<n;j++){
                if(target == matrix[i][j])
                    return true;
            }
        }
        return false;
    }
}
