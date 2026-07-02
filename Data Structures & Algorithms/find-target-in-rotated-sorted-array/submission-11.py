class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1


        while left <= right:
            mid = left + ( right-left+1 ) // 2

            if nums[mid] == target:
                return mid
            
            # left half is sorted
            if nums[left] <= nums[mid]:
                # checking if target exists in the left half
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    # target exists in the right half
            
                    left = mid + 1
            # right half is sorted
            else:
                # target exists in right half
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    # target exists in left half
                    right = mid - 1
        return -1