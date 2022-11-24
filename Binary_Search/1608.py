# 1608. Special Array With X Elements Greater Than or Equal X

def binarySearch(nums: list[int], target: int) -> int:
  l, r = 0, len(nums)
  while l < r: # Break when l = r or l > r  ## Might break in next loop if left = r-1
    m = (l+r) // 2 # m===left if left === r - 1 # e.g m=4 if left = 4 = r-1 = 5-1 since 9//2=4
    if nums[m] < target:
      l = m + 1 # Target must be on the Right ## Might interrupt while loop (l > r)
    else:
      r = m # Target must be on the Left or equal to m ## r > m > l
  return l

nums = [3,3,3,3,3]
nums = [a,b,c,d,e]
len(nums) == 5
# nums[target] = len(nums) - target == x 
# nums[mid] = len(nums) - mid == x && nums[mid-1] < x
print(binarySearch(nums,3))

# 0, 3, 3, 3, 4, 5

# 0, 3, [3], 4
# r=4 ----------> mid = 2 --> x = 2 && nums[2] = 3 > x 
# 0, [3], 3, 4
# r = mid = 2 --> mid = 1 -> x = 3  && nums[1] = 3 = x && nums[0] < x

# 0, 0, 0, [1]

# 3, 3, 3, 4