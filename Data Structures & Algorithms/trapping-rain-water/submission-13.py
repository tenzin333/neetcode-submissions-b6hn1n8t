class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0 
        right = n-1
        max_left = 0
        max_right = 0

        total_water = 0

        while left < right:

            if height[left] >= height[right]:
                max_right = max(max_right, height[right])
                total_water += max_right - height[right]
                right -= 1
            else:
                max_left = max(max_left, height[left])
                total_water += max_left - height[left]
                left += 1
        return total_water
