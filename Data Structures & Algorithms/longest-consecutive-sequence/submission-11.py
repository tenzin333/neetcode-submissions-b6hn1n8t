class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest_len = 0


        for num in numSet:
            if num-1 not in numSet:
                longest  = 1
                while num + longest  in numSet:
                    longest+=1
                longest_len = max(longest_len, longest)
        return longest_len