class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        r = ""
        for i in range(len(s)-1, -1 , -1):
            if str.isalnum(s[i]):
                r += s[i]

        t = ""
        for i in range(len(s)):
            if str.isalnum(s[i]):
                t += s[i]

        return r.lower() == t.lower() 
