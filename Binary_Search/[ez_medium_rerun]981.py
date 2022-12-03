# 981. Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.items = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.items.keys():
            self.items[key] = []
            self.timestamps[key] = []
            
        self.items[key].append(value)
        self.timestamps[key].append(timestamp)
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items.keys():
            return ""
        else:
            idx = self.binarySearch( self.timestamps[key], timestamp)
            if idx == len(self.timestamps[key]):
                return self.items[key][-1]
            if self.timestamps[key][idx] == timestamp:
                return self.items[key][idx]
            elif idx == 0:
                return ""
            else:
                return self.items[key][idx-1]
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
                
        return left