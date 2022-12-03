# 1011. Capacity To Ship Packages Within D Days (86.84%)

# Link:
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search
# optimized
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        prefix_sums = []
        prefix_sum = 0
        for w in weights:
            prefix_sum += w
            prefix_sums.append(prefix_sum)
        
        left, right = 0, prefix_sum
        min_cap = max(weights)
        
        # print(prefix_sums)
        while left < right:
            mid = left + (right-left)//2
            if mid < min_cap or not self.possibleCap(mid,weights,days):
                left = mid + 1 
            else:
                right = mid
        
        return left 

    
    def possibleCap(self, cap, weights, days):
        # print("cap: ",cap)
        curr_cap = 0
        curr_days = 1
        for w in weights:
            if curr_cap + w <= cap:
                curr_cap += w
            else:
                curr_days += 1
                if w < cap:
                    curr_cap = w
                else:
                    curr_cap = 0
                    curr_days += 1
        
        return True if days >= curr_days else False
                
    
    

        
                
        

# 2
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        prefix_sums = []
        prefix_sum = 0
        for w in weights:
            prefix_sum += w
            prefix_sums.append(prefix_sum)
        
        left, right = 0, len(prefix_sums)
        min_cap = max(weights)
        
        # print(prefix_sums)
        while left < right:
            mid = left + (right-left)//2
            if prefix_sums[mid] < min_cap or not self.possibleCap(prefix_sums[mid],weights,days):
                left = mid + 1 
            else:
                right = mid
        
        
        if left >= len(prefix_sums):
            return prefix_sums[-1]
        start = left - 1 if left > 0 else 0
        end = (left + 1) if (left+1) < (len(prefix_sums) -1) else -1
        # print(prefix_sums[start])
        # print(prefix_sums[end]+1)
        possible_caps = range(max(prefix_sums[start],min_cap),prefix_sums[end]+1)
        print(possible_caps)
        left, right = 0, len(possible_caps)
        
        while left < right:
            mid = left + (right-left)//2
            if self.possibleCap(possible_caps[mid], weights, days):
                right = mid
            else:
                left = mid + 1
        
        
        if left >= len(possible_caps):
            return possible_caps[-1]
        else:
            return possible_caps[left]
        # return possible_caps[left] if left < len(possible_caps) else prefix_sums[left]  # out of range
    
    def possibleCap(self, cap, weights, days):
        # print("cap: ",cap)
        curr_cap = 0
        curr_days = 1
        for w in weights:
            if curr_cap + w <= cap:
                curr_cap += w
            else:
                curr_days += 1
                if w < cap:
                    curr_cap = w
                else:
                    curr_cap = 0
                    curr_days += 1
        
        return True if days >= curr_days else False
                
    
    

        
                
        