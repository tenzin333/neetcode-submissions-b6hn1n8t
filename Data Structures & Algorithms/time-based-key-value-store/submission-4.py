# map = {
#             "alice": {
#                 "1": "happy"
#             }
#         }

class TimeMap:
    
    def __init__(self):
        self.store = {} # key -> (list of timestamps, list of value)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        left = 0
        right = len(arr) - 1
        ans = ""
        while left <= right:
            mid = left + (right - left + 1)//2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ans
        