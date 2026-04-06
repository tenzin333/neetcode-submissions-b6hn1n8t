class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i]  = True
                curr.append(nums[i])
                dfs(curr,used)
                curr.pop()
                used[i] = False
        dfs([], [False] * len(nums))
        return res