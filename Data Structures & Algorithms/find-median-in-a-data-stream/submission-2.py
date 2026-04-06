import heapq

class MedianFinder:
    def __init__(self):
        # Stores the smaller half of numbers. 
        # Max-Heap: we want the largest of the smalls.
        self.left_max_heap = [] 
        
        # Stores the larger half of numbers.
        # Min-Heap: we want the smallest of the larges.
        self.right_min_heap = [] 

    def addNum(self, num: int) -> None:
        # 1. Add to the left side (Max-Heap)
        # Use negative to simulate Max-Heap
        heapq.heappush(self.left_max_heap, -num)
        
        # 2. Balancing Act: Move the largest of the 'left' to the 'right'
        # This ensures every number in left <= every number in right
        val = -heapq.heappop(self.left_max_heap)
        heapq.heappush(self.right_min_heap, val)
        
        # 3. Maintain size property: 
        # Left side can have at most 1 more element than right
        if len(self.right_min_heap) > len(self.left_max_heap):
            val = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -val)

    def findMedian(self) -> float:
        if len(self.left_max_heap) > len(self.right_min_heap):
            return float(-self.left_max_heap[0])
        # If lengths are equal, median is the average of the two tops
        return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2.0