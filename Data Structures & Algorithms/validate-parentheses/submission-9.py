class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for bracket in s:
            if(brackets.get(bracket)):
                popped = stack.pop() if stack else None
                if(popped != brackets.get(bracket)):
                    return False
            else:
                stack.append(bracket)   
        return not stack