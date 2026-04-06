class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 2:
            return 1
        
        first = 1
        second = 1

        for _ in range(2, n+1):
            temp = second
            second = first + second
            first = temp
        return second