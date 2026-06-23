from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1 = len(s1)
        len_s2 = len(s2)
        right = len_s1
        freq1 = Counter(s1)
        left = 0
        while right <= len_s2:
            freq2 = Counter(s2[left:right])

            if freq1 == freq2:
                return True
            right+= 1
            left += 1
        return False

        