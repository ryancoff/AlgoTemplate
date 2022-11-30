#540. Single Element in a Sorted Array (96.95%)
import math 
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, math.ceil(len(nums)/2)
        # [3,3,7,7,10,10,11]
        # count(3,7,10,11)
        # mid = 2 ---> 2*mid = 4
        #  nums[2*mid] 
        # 2 4 5 7 ...
        # count = index * 2
        # First one odd
        # count(3,7,10,11,12)
        # [3,3,7,7,10,11,11,12,12]
        while left < right:
            mid = left + (right-left)//2
            if nums[mid*2-1] < nums[mid*2] or mid == 0:
                left = mid + 1
            else:
                right = mid
        return nums[(left-1)*2]

# Similar Problems
# 287
