from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left = 0 
        right = 0
        freqt = Counter(t)
        window = defaultdict(int)
        ns = len(s)
        res, resLen = [-1, -1], float('infinity')
        l = 0 
        have, need = 0, len(freqt)

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in freqt and window[c] == freqt[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in freqt and window[s[l]] < freqt[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
