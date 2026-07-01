class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

    # k = 1
    #     (1 / 1 ) * 1= 1
    #     4 / 1 *  = 4
    #     3 /  1 = 3
    #     2 / 1  = 2 
    #     toatl = 10 > 9

    # k = 2
    #     1 / 2 = 0.5 = 1
    #     4 / 2 = 2
    #     3 / 2 = 1.5 = 2
    #     2 / 2 = 1
    #     total = 6

        peak = max(piles)
        min_rate = float('infinity')

        left = 1
        right = peak

        while left <= right:
            total_time_taken = 0
            rate = left + (right - left + 1) // 2
            for pile in piles:
                total_time_taken += math.ceil(pile / rate)
            if total_time_taken > h:
                left = rate + 1
            else:
                min_rate = min(rate, min_rate)
                right = rate - 1
        return 0 if min_rate == float('infinity') else min_rate
            

    
