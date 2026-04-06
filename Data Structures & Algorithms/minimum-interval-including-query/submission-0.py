class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
            basically i need to count the interval length, 
            for a given query against a give intervals

        '''
        if not intervals:
            return []

        intervals.sort(key = lambda x: x[0])
        res = []

        for query in queries:
            new_query = float('inf')
            for interval in intervals:
                if query>= interval[0] and query<=interval[1]:
                    new_query = min(new_query, interval[1]-interval[0]+1)
            if new_query ==  float('inf'):
                new_query = -1
            res.append(new_query)
        return res

