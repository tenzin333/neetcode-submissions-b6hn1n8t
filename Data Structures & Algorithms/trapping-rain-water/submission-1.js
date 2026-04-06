class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const size = height.length;
        let water = 0;
        for(let i=0;i<size;i++){
            let leftMax=0;
            let rightMax=0;

            for(let l=0;l<=i;l++){
                leftMax = Math.max(height[l],leftMax);
            }

            for(let r=i;r<size;r++){
                rightMax = Math.max(height[r],rightMax);
            }

            water += Math.min(leftMax,rightMax) - height[i];
        }
        return water;

    }
}
