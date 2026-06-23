class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            max_area = max(max_area, height * width)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1


        return max_area