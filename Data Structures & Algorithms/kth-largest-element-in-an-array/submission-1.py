import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = []

        for n in nums:
            heapq.heappush(self.heap, n)

            if len(self.heap) > k:
                heapq.heappop(self.heap)

        return self.heap[0]