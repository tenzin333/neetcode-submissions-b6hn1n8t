class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        

        left = 1
        right = max(piles)

        ans = float('inf')
        while left <= right:
            rate = left + (right - left + 1) // 2
            total_time = 0
            for pile in piles:
                total_time +=  math.ceil( pile / rate )
            if total_time > h:
                left = rate  + 1
            else:
                right = rate - 1
                ans = min(ans, rate)


        return ans
