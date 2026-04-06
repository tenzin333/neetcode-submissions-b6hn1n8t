class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const size = height.length;
        let water = 0;

        for(let i=0;i<size;i++){
            let left=0; 
            let right = 0;

            for(let l=0;l<=i;l++){
                left = Math.max(left,height[l]);
            }

            for(let r=i;r<size;r++){
                right = Math.max(right,height[r]);
            }

            water += Math.min(left,right)-height[i];
        }
        return water;
    }
}
