class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
          const size = heights.length;
          let area = 0;
          let left =0;
          let right = size-1;

          while(left<right){
            const height = Math.min(heights[left],heights[right]);
            const width =  (right-left);
            area = Math.max(area, height*width);

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
          }

        return area;
    }
}
