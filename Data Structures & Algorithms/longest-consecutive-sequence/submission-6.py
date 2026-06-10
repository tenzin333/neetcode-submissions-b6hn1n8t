class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxLength = 0
        numSet = set(nums)

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                curr = num+1
                while curr in numSet:
                    length += 1
                    curr += 1
                maxLength = max(maxLength, length)
        return maxLength