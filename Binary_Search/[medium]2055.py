# 2055. Plates Between Candles (86.88%)
import bisect

#1
class Solution:
    def platesBetweenCandles(self, s, queries):
        A = [i for i,c in enumerate(s) if c == '|']
        res = []
        for a,b in queries:
            i = bisect.bisect_left(A, a)
            j = bisect.bisect(A, b) - 1
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res

# 2 
class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        # self.prefix_sums = []
        self.candle_idxs = []
        ret = []
        # prefix_sum=0
        for idx, item in enumerate(s):
            if item == "*":
                # prefix_sum += 1
                pass
            else:
                self.candle_idxs.append(idx)
            # self.prefix_sums.append(prefix_sum)
            
        # self.total_sum = prefix_sum
        
        # print("prefix_sums: ",self.prefix_sums)
        # print("candle_idxs: ",self.candle_idxs)
        
        for q in queries:
            # q[0] && q[1]
            if q[0] == q[1] - 1:
                ret.append(0)
                continue
            lo_idx = self.binarySearch(self.candle_idxs, q[0], False)
            hi_idx = self.binarySearch(self.candle_idxs, q[1], True)
            # print("lo_idx: ",lo_idx)
            # print("hi_idx: ",hi_idx)
            # pos_diff = (hi_idx-lo_idx) if (hi_idx-lo_idx) > 0 else 0
            ret.append(self.candle_idxs[hi_idx]-self.candle_idxs[lo_idx]-(hi_idx-lo_idx) if (hi_idx-lo_idx) > 0 else 0)
            
            
        return ret
    
    def binarySearch(self,nums, target, isHigh):
        # print("length of nums: ",len(nums))
        # print("target: ",target)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left)//2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid

 
        # out of range
        if left == len(nums) or (nums[left] > target and left > 0 and isHigh):
            return left -1
        # 100
        return left
                
                
                
        