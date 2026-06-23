class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
   
        n = len(nums)

        answers = set()
        for i in range(n-2):
            freq = {}
            for j in range(i+1,n):
                a = nums[i]
                b = nums[j]
                c = -1 * (a+b)

                if c in freq:
                    answers.add(tuple(sorted((a,b,c))))
                
                freq[b] = j
        return [list(t) for t in answers]