class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        const n = heights.length;
        let area  = 0;
        let stack  = [];
        for(let i=0;i<=n;i++){
            const h = (i==n) ? 0: heights[i];
            while(stack.length && h<heights[stack[stack.length-1]]){
                const height = heights[stack.pop()];
                const width = (stack.length==0) ? i : i-stack[stack.length-1]-1;
                area =Math.max(area, height*width);
            }
            stack.push(i);
        }
        return area;
    }
    
}
