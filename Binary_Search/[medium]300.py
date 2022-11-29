# 300. Longest Increasing Subsequence (97.14%)
from bisect import bisect_left

# Binary Seach on temporary result
class Solution:  # 68 ms, faster than 93.92%
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)

# Time exceed
# Binary Seach on given information/ input array
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            # print(f"{mid} -- {self.checkSubWithLength(nums,mid)}")
            if self.checkSubWithLength(nums,mid):
                left = mid + 1
            else:
                right = mid
        # print("left: ",left)
        return left if self.checkSubWithLength(nums,left) else left-1
            
    
    def checkSubWithLength(self,nums,length):
        # Given increasing list
        # if length == len(nums):
        #     return self.isIncreasingSubWithLengthExited(nums,0,length)
        # Include starting pos
        for i in range(len(nums)-length+1):
            # print(f"Outside: {i} {length}")
            if self.isIncreasingSubWithLengthExited(nums,i,length):
                return True
        return False

    def isIncreasingSubWithLengthExited(self,nums,start,length):
        if length == 1:
            return True
        
        # end = start+length if (start+length < len(nums)) else len(nums)-1
        # print(f"Inside {start} {end} {length}")
        
        # Might exclude "end" if range(start+1,end)
        # Can't fix "end" --> Need to check all pos e.g 11,12,13,14,15,6,7,8,101,18
        # for index in range(start+1,end+1):
        
        for index in range(start+1,len(nums)):
            if nums[start] < nums[index]:
                if self.isIncreasingSubWithLengthExited(nums,index,length-1):
                   return True
            
        # left, right = (start+1), len(nums)
        # while left < right:
        #     mid = left + (right-left)//2
        #     if nums[start] >= nums[mid]:
        #         left = mid + 1
        #     else: # <=
        #         if self.isIncreasingSubWithLengthExited(nums,mid,length-1):
        #             return True
        #         else: #
        #             right = mid
                
        return False