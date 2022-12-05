#2008. Maximum Earnings From Taxi (%70.59)

"""
Releated Question: 1235
"""

# Optimized
import bisect

class Solution:
    def maxTaxiEarnings(self, n, rides):
        rides = sorted(rides)
        S = [i[0] for i in rides]
        
        m = len(rides)
        dp = [0]*(m+1)
        for k in range(m-1, -1, -1):
            temp = bisect.bisect_left(S, rides[k][1])
            dp[k] = max(dp[k+1], rides[k][2] - rides[k][0] + rides[k][1] + dp[temp])
            
        return dp[0]

# Best Yeid (A+1)---> (?) Yeid (A) 
# Cool Yeil (B)---> (?) Yeid (A)

# Best Yied (A+1) > Cool (B+A) ---> Best Yield (A+1)=(A)


# Z--> A

# Original
class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        self.start_points = [r[0] for r in rides]
        self.length = len(self.start_points)
        self.sorted_indices = sorted(range(self.length), key=lambda k: self.start_points[k]) 
        self.cache_dollars = [0]*(self.length+1)

        curr_max = 0
        for idx in range(self.length-1,-1,-1):
            next_idx = self.binarySearch( 0, rides[self.sorted_indices[idx]][1])
            self.cache_dollars[idx] = max(self.cache_dollars[idx+1], self.calRideEarning(rides[self.sorted_indices[idx]]) + self.cache_dollars[next_idx])
        
        return self.cache_dollars[0]
    
    
    def calRideEarning(self, ride):
        return ride[1]-ride[0]+ride[2]
        
    def binarySearch(self, possible_start, target):
        left, right = possible_start, self.length # - 1 not check left = right = length - 1 = 0
        
        while left < right:
            mid = left + (right-left)//2
            if self.start_points[self.sorted_indices[mid]] < target:
                left = mid + 1
            else:
                right = mid
        
        return left 
        
        # [[1, 5, 3], [1, 6, 10], [2, 6, 2], [4, 10, 8], [5, 6, 10], [5, 6, 4], [5, 10, 1], [7, 9, 6], [8, 10, 9], [9, 10, 5]]
        # At [5, 10, 1] from [8, 10, 9] found [9, 10, 5] --> return -1
        # At [1, 5, 3] from [2, 6, 2] found [5, 10, 1] ---> remove elif self.start_points[self.sorted_indices[mid]] == target: --> return left_side