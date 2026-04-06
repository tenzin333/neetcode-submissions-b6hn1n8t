import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = []

        for n in nums:
            heapq.heappush(self.heap, -n)
        ans = 0
        while k > 0:
            ans = - heapq.heappop(self.heap)
            k-=1 
        return ans