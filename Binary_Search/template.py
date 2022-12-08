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

# 3 3 3 3
# Search Insert Position
# First Appearance
# Possible Insertion
def binarySearch(nums: list[int], target: int) -> int:
  l, r = 0, len(nums)
  while l < r: # Break when l = r or l > r  ## Might break in next loop if left = r-1
    m = (l+r) // 2 # m===left if left === r - 1 # e.g m=4 if left = 4 = r-1 = 5-1 since 9//2=4
    if nums[m] < target:
      l = m + 1 # Target must be on the Right ## Might interrupt while loop (l > r)
    else:
      r = m # Target must be on the Left or equal to m ## r > m > l
  return l

nums = [1,4,7,11,15]
print(binarySearch(nums,10))