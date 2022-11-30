# 35. Search Insert Position (90%)
class Solution:
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)
        while l < r: 
            mid=(l+r)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid # while l<=r && target is found --> Infinity loop
        return l