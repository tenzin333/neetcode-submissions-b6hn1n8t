import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i, num in enumerate(nums):
            # Push current element
            heapq.heappush(heap, (-num, i))

            # Remove elements outside the window
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)

            # First window is formed
            if i >= k - 1:
                res.append(-heap[0][0])

        return res