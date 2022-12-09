# 2187. Minimum Time to Complete Trips (99.81%)

# Cleaner
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 0, min(time)*totalTrips
        
        while lo < hi:
            m = (lo+hi)//2
            trips = sum([m//t for t in time])
            if trips >= totalTrips:
                hi = m
            else:
                lo = m + 1

            
        return hi
# 1
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_t = min(time) # Might no need

        upperBound = math.ceil(totalTrips*min_t) # total/fastest_velocity
        # print("upperBound: ",upperBound)
        left, right = 0, upperBound
        while left < right:
            mid = left + (right - left)//2
            if self.calCurrentTrips(time,mid) < totalTrips:
                left = mid + 1
            else:
                right = mid
        
        # print("Left & total:",self.calCurrentTrips(time,left))
        # print("Left: ", right)
        if self.calCurrentTrips(time,left-1) >= totalTrips:
            # print("Here!")
            return left-1  
        else:
            return left

    def calCurrentTrips(self, time, currTime):
        return sum(currTime//t for t in time)