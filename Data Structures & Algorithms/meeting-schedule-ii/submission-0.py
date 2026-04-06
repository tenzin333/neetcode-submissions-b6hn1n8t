import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        
        # sort by start time
        intervals.sort(key=lambda x: x.start)
        
        heap = []  # stores end times
        
        # add first meeting
        heapq.heappush(heap, intervals[0].end)
        
        for interval in intervals[1:]:
            
            # if the earliest meeting ended before this one starts
            if interval.start >= heap[0]:
                heapq.heappop(heap)  # reuse the room
            
            # add current meeting's end time
            heapq.heappush(heap, interval.end)
        
        return len(heap)