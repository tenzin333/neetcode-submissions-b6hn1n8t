class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = slow_car = 0

        for p, s in sorted(zip(position, speed), reverse = True):
            eta = (target - p) / s

            if eta > slow_car:
                slow_car = eta
                ans+= 1
        return ans
