class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        maxf = 0
        counter = {}
        res = 0
        for right in range(len(s)):
            counter[s[right]] = 1 + (counter.get(s[right] , 0))
            maxf = max(maxf, counter[s[right]])

            while (right-left+1) - maxf > k:

                counter[s[left]] -=1
                left+=1
            res = max(res, right-left+1)
        return res
