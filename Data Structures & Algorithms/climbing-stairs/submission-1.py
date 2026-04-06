class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''

            f(n) = f(n-1) + f(n-2)
            f(2) = f(1) + f(0) = 1+1= 2

        '''
        if n < 2:
            return 1
        first = 1
        second = 1

        for i in range(2,n+1):
            temp =  second
            second = first + second
            first = temp
        return second