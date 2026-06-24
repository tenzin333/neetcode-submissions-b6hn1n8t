from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        left = 0 
        right = n1
        freq1 = Counter(s1)

        while right <= n2:
            freq2  = Counter(s2[left:right])
            if freq2 == freq1:
                return True
            right += 1
            left += 1 
        return False
