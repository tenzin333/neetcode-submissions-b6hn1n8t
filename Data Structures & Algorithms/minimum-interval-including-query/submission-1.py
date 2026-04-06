class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort(key= lambda x: x[0])
        output = []
        for query in queries:
            new_val = float('inf')
            for interval in intervals:
                start,end = interval[0], interval[1]
                if start<=query and query<=end:
                    new_val = min(new_val, end-start+1)
            if new_val == float('inf'):
                new_val=-1
            output.append(new_val)
        return output