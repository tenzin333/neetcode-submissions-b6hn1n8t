class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # Case 1: Current interval is completely BEFORE newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # Case 2: Current interval is completely AFTER newInterval
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                # Optimization: since we found the spot, just return everything remaining
                return res + intervals[i:]
            
            # Case 3: Overlap! Update the newInterval to be the 'merged' version
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # If the loop finishes, we still need to add the (possibly merged) newInterval
        res.append(newInterval)
        return res