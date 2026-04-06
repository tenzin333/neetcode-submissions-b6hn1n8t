import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = Counter(nums)
        heap = []
        for num,freq in freqCount.items():
            heapq.heappush(heap, (-freq,num))
        
        res = []

        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res