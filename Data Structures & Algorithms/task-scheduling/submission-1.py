from collections import Counter
import heapq



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [ -ctr  for ctr in counter.values()]

        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q :
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                ctr = 1 + heapq.heappop(maxHeap)
                if ctr:
                    q.append([ctr, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


        