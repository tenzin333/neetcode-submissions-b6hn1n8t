class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        ans = right 
        while left<=right:
            speed = left  + (right-left)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)

            if time <= h:
                ans  = speed
                right = speed -1
            else:
                left= speed +1
        return ans
