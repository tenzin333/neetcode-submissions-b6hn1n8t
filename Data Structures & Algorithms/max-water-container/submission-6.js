class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length-1;
        
        let maxArea = 0;

        while(left < right){
            let l = Math.min(heights[left], heights[right]);
            let w = right - left;
            let area = l * w;

            maxArea  = Math.max(area, maxArea);

            if(heights[left] < heights[right]){
                left++;
            }else{
                right --;
            }

        }
        return maxArea;
    }
}
