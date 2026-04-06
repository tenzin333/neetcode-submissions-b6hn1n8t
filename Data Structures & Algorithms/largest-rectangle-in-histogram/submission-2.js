class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        const size = heights.length;
        let area  = 0;
        for(let i=0;i<size;i++){
            let minHeight = heights[i];
            for(let j=i;j<size;j++){
                    const width = j-i+1;
                    minHeight = Math.min(minHeight,heights[j]);
                    area = Math.max(area,width*minHeight);
            }
        }

        return area;
    }
}
