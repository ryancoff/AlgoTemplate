"""
Video: https://www.youtube.com/watch?v=MFhxShGxHWc
Template List: https://www.piratekingdom.com/leetcode/templates

"""

def binarySearch(nums: list[int], target: int) -> int:
  l, r = 0, len(nums)
  while l < r: # Break when l = r or l > r  ## Might break in next loop if left = r-1
    m = (l+r) // 2 # m===left if left === r - 1 # e.g m=4 if left = 4 = r-1 = 5-1 since 9//2=4
    if nums[m] < target:
      l = m + 1 # Target must be on the Right ## Might interrupt while loop (l > r)
    else:
      r = m # Target must be on the Left or equal to m ## r > m > l
  return l

nums = [1, 2, 3, 3, 3, 6, 9];


"""
if l===r
then l=mid+1 > r

NOT FOUND --> l = m+1

if l===r-1 -> mid = (l+r)//2 = r - 1
then l=mid+1 === r
"""

"""
condition l < r:

m > l <=> l < r

m = l <=> l = r

"""

"""
Leetcode:

Sqrt(x)
Search Insert Position
"""