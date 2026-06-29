class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets =  {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        stack = []

        for i in range(len(s)):
            paran = s[i]

            if paran in ["{", "[" , "("]:
                stack.append(paran)
            else:
                if   (stack and paran != brackets[stack[-1]]) or not stack:
                    return False
                stack.pop()
        return True if len(stack)==0 else False
