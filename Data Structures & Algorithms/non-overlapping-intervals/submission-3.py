class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
            if start of next is greater or eq to end of prev then update the prevend with curr end
            else we update the prev end with min end and update count
        '''
        intervals.sort(key= lambda x: x[0])

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start>= prevEnd:
                prevEnd = end
            else:
                res+=1
                prevEnd = min(prevEnd, end)
        return res
