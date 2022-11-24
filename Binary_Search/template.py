"""
Video: https://www.youtube.com/watch?v=MFhxShGxHWc
Template List: https://www.piratekingdom.com/leetcode/templates

"""

"""
Leetcode:
704. Binary Search

Sqrt(x)
Search Insert Position
"""
# Search Insert Position
def binarySearch(nums: list[int], target: int) -> int:
  l, r = 0, len(nums)
  while l < r: # Break when l = r or l > r  ## Might break in next loop if left = r-1
    m = (l+r) // 2 # m===left if left === r - 1 # e.g m=4 if left = 4 = r-1 = 5-1 since 9//2=4
    if nums[m] < target:
      l = m + 1 # Target must be on the Right ## Might interrupt while loop (l > r)
    else:
      r = m # Target must be on the Left or equal to m ## r > m > l
  return l

# nums = [1, 2, 3, 3, 3, 6, 9];
# Insert 4 --> 

"""
l < r ---> l < m < r
l = m + 1 --> l <= r
l < r = m
m = (l+r) // 2 ----> m = l if l = r - 1 ----> l = m + 1 = r -----> break ----> return m + 1 with nums[m] < target
"""


# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2 # Index
            mid_v = nums[mid]
            left_v = nums[left]
            right_v = nums[right]
            print(f"Mid: {mid_v}, Left: {left_v}, Right: {right_v}")
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
            
        return -1