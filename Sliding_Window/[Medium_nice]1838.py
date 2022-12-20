# 1838. Frequency of the Most Frequent Element
# Guide: https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/c-maximum-sliding-window-cheatsheet-template/?orderBy=most_votes

# Optimized (100%) (Non-shrinkable)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        nums.sort()

        for r in range(len(nums)):
            k += nums[r]

            if k < (r - l + 1) * nums[r]:
                k -= nums[l]
                l += 1
        
        return r - l + 1

# Template (87%)

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j,ans = 0,0,1
        sum = 0
        N = len(nums)
        for j in range(N):
            sum += nums[j]
            while k < nums[j]*(j - i + 1) - sum:
                sum -= nums[i] # Update sum = shrink left
                i += 1
            ans = max(ans,j-i+1)
        return ans
    
# Template 2 (Non-shrinkable) (Faster) (97.90%)
# GROW = Move Right when valid, and SHIFT = SHRINK = Move Left when invalid
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j,N = 0,0,len(nums)
        sum = 0
        for j in range(N):
            sum += nums[j]
            if k < nums[j]*(j - i + 1) - sum:
                sum -= nums[i] # Update sum = shrink left
                i += 1
        return j-i+1