class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let water = 0;
        for(let i=0;i<height.length;i++){
            let leftMax = 0,rightMax=0;

            for(let l=0;l<=i;l++){
                leftMax = Math.max(leftMax,height[l]);
            }

            for(let r=i;r<height.length;r++){
                rightMax = Math.max(rightMax,height[r]);
            }

            water += Math.min(leftMax,rightMax) - height[i];
        }
        return water;

    }
}
