class MedianFinder:

    def __init__(self) -> None:
        self.values = []

    def addNum(self, val: int) -> None:
        self.values.append(val)

    def findMedian(self) -> float:
        n = len(self.values)
        self.values.sort()
        mid = (n) // 2
        if n % 2 == 0:
            return (self.values[mid-1] + self.values[mid]) / 2.0
      
        return self.values[mid]

        