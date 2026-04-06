import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 2 3 6 2 4
        # 6 > 4 , 6-4 = 2 , 2 3 2 2
        # 3 > 2 , 3-2 = 1 , 2 1 2 
        # 2  2  , [1]
        self.heap = []
        
        for stone in stones:
            heapq.heappush(self.heap,-stone)

        # -2 -3 -6 -2 -4 =>   -6 -4 -3 -2 -2
        while len(self.heap) > 1 :
            stone1 = - heapq.heappop(self.heap)
            stone2 = - heapq.heappop(self.heap)
            answer = 0
            if stone1 > stone2 :
                answer = stone1 - stone2 
            elif stone1 < stone2 :
                answer = stone2 - stone1 
            else: 
                answer = 0 
            heapq.heappush(self.heap , -answer)
        return -self.heap[0]


        


