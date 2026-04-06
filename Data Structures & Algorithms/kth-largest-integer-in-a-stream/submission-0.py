class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.mapped = { k : nums}
        
    def add(self, val: int) -> int:

        streams = self.mapped[self.k]
        streams.append(val)
        self.mapped[self.k] = streams
        streams.sort(reverse=True)
        return streams[self.k-1]

        
