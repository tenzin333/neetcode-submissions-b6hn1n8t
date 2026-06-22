class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        seen = set(nums)

        longest_len = 0


        for num in seen:
            if num-1 not in seen:
                longest = 1
                curr = num +1

                while curr in seen:
                    longest += 1
                    curr += 1
                
                longest_len = max(longest_len, longest)
        return longest_len