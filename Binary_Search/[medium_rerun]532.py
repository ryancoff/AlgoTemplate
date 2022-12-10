
# 532. K-diff Pairs in an Array (92%)
# Hash Map
from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result

# Binary Search (Not Good)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ret = set()
        nums = sorted(nums)
        for lo in range(len(nums) - 1): 
            idx = self.binarySearch(nums[lo+1:],k + nums[lo])
            if lo+1+idx > len(nums) - 1:
                continue
            if nums[lo+1+idx] - nums[lo] == k:
                ret.add((nums[lo],nums[lo+1+idx]))

        return len(ret)
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left