# 875. Koko Eating Bananas (78.74%)
# 1
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        # self.prefix_sums = []
        prefix_sum = 0
        for p in piles:
            prefix_sum += p
            # self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
        extra_hr = 1 if self.total_sum%h else 0
        possible_speed = self.total_sum//h + extra_hr
        # print("possible_speed: ",possible_speed)
        if len(piles) == 1:
            return possible_speed
        
        left, right = 0, len(piles)
        while left < right:
            mid = left + (right-left)//2
            # if piles[mid]*(h-mid-1) < (self.total_sum - self.prefix_sums[mid]):
            if h-mid < self.timeLeft(piles,mid,piles[mid]):
                left = mid + 1
            else:
                right = mid
        # print("Left: ",left)
        # possible_speed = piles[left-1] if piles[left-1] > possible_speed else possible_speed
        if (h-left) < self.timeLeft(piles,left,piles[left]-1):
            return piles[left]
        else:
            # for k in range(possible_speed,piles[left]+1):
            #     # if k*(h-left-1) >= (self.total_sum - self.prefix_sums[left] + piles[left]-k):
            #     if (h-left) >= self.timeLeft(piles,left,k):
            #         return k
            left_2, right_2 = possible_speed, piles[left]+1
            while left_2 < right_2:
                mid_2 = left_2 + (right_2 - left_2)//2
                if h-left < self.timeLeft(piles,left,mid_2):
                    left_2 = mid_2 + 1
                else:
                    right_2 = mid_2
            return left_2
        return piles[left]
    
    def timeLeft(self,piles,pos,speedAtPos):
        estimated_time = 0
        for index in range(pos,len(piles)):
            extra_hr = 1 if piles[index]%speedAtPos else 0 #piles[pos]
            est = piles[index]//speedAtPos + extra_hr
            estimated_time += est
            
        return estimated_time # include time at current pos
        
        
# Optimized Sol (99.32%)
a = None
from math import ceil
def solve(x, h):
    # print([ceil(i/x) for i in a], h)
    return sum([ceil(i/x) for i in a]) <= h

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        global a
        a = piles
        l = 1
        r = max(a)
        mid = (l + r) // 2
        while l < r:
            if solve(mid,h):
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2
        return mid
        

# LeetCode Sol
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right


# [30,11,23,4,20]
# [4,11,20,23,30]
# total = 88
#  4 11 [18] 20 23 30
#  1  2  3
#  time_left = h - 3 = 2
#  time_left*18 < 88

# 1 2 3 4


# 4 11 20 23 30  # nums
# 4 15 35 58 88  # totalBananasAtCurrentSpeed
# total = 88
# left, right = 0, len(nums)
# while left < right
# mid = left + (right-left)//2
# mid = 2 ---> nums[mid]*(h-mid-1)=20*2=40 < totalBananas - totalBananasAtCurrentSpeed = 88 - 35 = 53
# --> left = mid + 1

# 4 11 20 23 30
# 4 11 19 1 19 4 19 11

# 4 11 20 20 3 20 10
# mid = 2 ---> timeLeft = h-mid-1 = 3 < est_hours = 4 
# mid = 2 ---> nums[mid]*(h-mid-1)=20*3=60 > totalBananas - totalBananasAtCurrentSpeed = 88 - 35 = 53


[312884470]
312884469

[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
823855818

[1000000000,1000000000]
3
# 4 11 20 23 30
# 4 11 15 5 15 5 15 15 5

# 9 1 9 1