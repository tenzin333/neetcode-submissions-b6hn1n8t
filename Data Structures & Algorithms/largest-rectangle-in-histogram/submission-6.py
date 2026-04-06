class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)

        maxArea= 0

        for i,h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                        height = heights[stack[-1]]
                        stack.pop()

                        if not stack:
                                width = i
                        else :
                                width  = i - stack[-1]-1
                        maxArea = max(maxArea, height * width)
                stack.append(i)
        return maxArea