# 362. Design Hit Counter (98.48%)

from collections import deque


class HitCounter:

    def __init__(self):
        self.nums = []
        self.totalHit = []
        

    def hit(self, timestamp: int) -> None:
        self.nums.append(timestamp)
        if len(self.totalHit) == 0:
            self.totalHit.append(1)
        else:
            self.totalHit.append(self.totalHit[-1]+1) 
        
    def getHits(self, timestamp: int) -> int:
        length = len(self.nums)
        if length > 1:
            if (timestamp - self.nums[0]) >= 300:
                first_hit = self.binarySearch(timestamp - 299)
                self.totalHit = [x - self.totalHit[first_hit-1] for x in self.totalHit]
                self.totalHit = self.totalHit[first_hit:]
                self.nums = self.nums[first_hit:]
            # else:
            ret = self.totalHit[-1]
        elif length == 1:
            if (timestamp - self.nums[0]) >= 300:
                ret = 0
                self.totalHit = []
                self.nums = []
                
            else:
                ret = self.totalHit[0]
        else:
            ret = 0
        return ret
        
        
    def binarySearch(self, target):
        left, right = 0, len(self.nums)
        while left < right:
            mid = left + (right-left)//2
            if self.nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
                
# Queue
class HitCounter:

    def __init__(self):
        self.queue = deque([])        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)                
        

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] + 300 <= timestamp:
            self.queue.popleft()
        return len(self.queue)



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# [0,2*1e9]
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]


#
# [0,2*1e9]
# left, right = 0, len(nums)
# mid = left + (right-left)//2
#

# Search for the begginning of past 300 seconds
# Nums : List of timestamps ---> nums[mid] = timestamp
# NUms : list of hits ----> nums[mid] == no hit
# 
# Condition: Timestamp = 300 + index  ==> (index, 300+index] ==> [index + 1, 300 + index]
#  1 2 3 4
#  1
#  2 1
#  3 2 1
#  # # # #

#  1 2 3 4 300
#  4 3 2 # 1
#  # # # # #
#  1 2 3 4 300 301
#  1 2 3 #  4   4-1
#  4 3 2 # 1   # 
#  pop()
#  2 3 4 300 301
#  3 2 #  1   #

# 599 hit
# 599 = 299 + 300 ==> [300,599]
#  2 3 4 300 301 599
#  3 2 #  1   #   ?
#  ([300:]).append(599)
#  300 301 599
#   2   #   1
#   

# 100 100 100 102 103 105 105 105 .......... 105 105 ..... 399 400
# Target = timestamp
# Nums: List of timestamp
# mid = left + (right-left)//2
# target = timestamp (passed in getHit) - 300 + 1

# binarySearch(nums,target) --> index
# ---> ret =  totalHit[index]
# nums = nums[index:]
# totalHit = totalHit[index:]

totalHit = [1]
totalHit.append(0)
totalHit = [x+1 for x in totalHit]
print(totalHit)
