class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        
        for token in tokens:
                if token in operators:
                        match token:
                                case "+":      
                                        a = int(stack.pop())
                                        b = int(stack.pop())

                                        stack.append(a+b)
                
                                case "-": 
                                        a = int(stack.pop())
                                        b = int(stack.pop())
                                        stack.append(b - a)
                                case "*":
                                        a = int(stack.pop())
                                        b = int(stack.pop())
                                        stack.append(b * a)
                                
                                case "/":
                                        a = int(stack.pop())
                                        b = int(stack.pop())
                                        stack.append(int(b/a))
                                        
                                case _:
                                        return None
                else:
                        stack.append(int(token))
        return stack[-1]