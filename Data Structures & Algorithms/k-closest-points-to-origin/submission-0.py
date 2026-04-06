import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        self.heap = []
        
        for x , y in points:
            dist = x**2 + y **2
            heapq.heappush(self.heap, (dist, [x,y]))

        res = []
        for _ in range(k):
            points = heapq.heappop(self.heap)
            res.append(points[1])
        return res