class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
          const size = heights.length;
          let area = 0;
          for(let i=0;i<size-1;i++){
            for(let j=i+1;j<size;j++){
                const height = Math.min(heights[i],heights[j]);
                const width = (j-i);
                area = Math.max(area,(height*width));
            }
          }
        return area;
    }
}
