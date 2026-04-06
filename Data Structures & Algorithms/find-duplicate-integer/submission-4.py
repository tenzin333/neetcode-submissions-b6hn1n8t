class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast starts at nums[0]
        slow = fast = nums[0]
        # find the intersection slow == fast
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # start from nums[0] to slow while slow!=slow2 
        slow2 = nums[0]
        while slow!= slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
        # return slow