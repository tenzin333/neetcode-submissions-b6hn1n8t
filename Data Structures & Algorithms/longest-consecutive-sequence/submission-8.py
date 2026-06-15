class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        finalAns = 0
        numsSet = set(nums)
        for num in numsSet:
            if num-1 not in numsSet:
                length = 1
                curr = num
                while curr + 1 in numsSet:
                    length += 1
                    curr += 1
                finalAns = max(length, finalAns)
        return finalAns