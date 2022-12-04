# 162. Find Peak Element (99.79%)
"""
Good Guidline:
https://leetcode.com/problems/find-peak-element/discuss/1290642/Intuition-behind-conditions-or-Complete-Explanation-or-Diagram-or-Binary-Search

"""
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        
        left, right = 0, length
        
        while left < right:
            mid = left + (right-left)//2
            
            if mid == 0 and nums[mid] < nums[mid+1]:
                left = mid + 1
            elif mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] and mid == length - 1:
                return mid
            elif nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid] and mid == length - 1:
                right = mid
            # elif nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
            #     right = mid
            else: # > <
                right = mid
        
        if left == 0:
            nums[left] > nums[left+1]
            return left
        if right == length - 1:
            nums[right-1] < nums[right]
            return right
                
# shorten version
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        # left == right
        # left - 1 = 0 - 1 = -1 => nums[-1] == nums[0]
        # if nums[left-1] > nums[left]:
        #     return left - 1
        return left

# Not Worked Version
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            # mid >= left
            # mid >= 0
            # mid == 0
            # mid-1 = - 1
            if nums[mid-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        # left == right
        # left - 1 = 0 - 1 = -1 => nums[-1] == nums[0]
        # if nums[left-1] > nums[left]:
        #     return left - 1
        return left

# Not Worked Version 2
