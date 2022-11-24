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
def binarySearch(nums: list[int], target: int) -> int:
  l, r = 0, len(nums)
  while l < r: # Break when l = r or l > r  ## Might break in next loop if left = r-1
    m = (l+r) // 2 # m===left if left === r - 1 # e.g m=4 if left = 4 = r-1 = 5-1 since 9//2=4
    if nums[m] < target:
      l = m + 1 # Target must be on the Right ## Might interrupt while loop (l > r)
    else:
      r = m # Target must be on the Left or equal to m ## r > m > l
  return l


nums = [0, 0, 3, 3, 4]
left, right = 0,len(nums)
mid = (left+right)//2
print("Mid: ", mid)
special_value = len(nums) - binarySearch(nums,mid)
print("# elemnents: ",special_value) # > mid ==> increase mid
print(f"Is {mid} a special x",special_value == mid)
# mid = 2 (no)
left = mid + 1
mid = (left+right)//2
print("Mid: ", mid)
special_value = len(nums) - binarySearch(nums,mid)
print("# elemnents: ",special_value) # < mid ==> decrease mid
print(f"Is {mid} a special x",special_value == mid)

# mid = 4 (no)
right = mid
mid = (left+right)//2
print("Mid: ", mid)
special_value = len(nums) - binarySearch(nums,mid)
print("# elemnents: ",special_value) # 
print(f"Is {mid} a special x",special_value == mid)
print("Array is Special ")


# nums = [0, 3, 3, 3, 4]
# left, right = 0,len(nums)
# mid = (left+right)//2
# print("Mid: ", mid)
# special_value = len(nums) - binarySearch(nums,mid)
# print("# elemnents: ",special_value) # > mid ==> increase mid
# print(f"Is {mid} a special x",special_value == mid)
# # mid = 2 (no)
# left = mid + 1
# mid = (left+right)//2
# print("Mid: ", mid)
# special_value = len(nums) - binarySearch(nums,mid)
# print("# elemnents: ",special_value) # < mid ==> decrease mid
# print(f"Is {mid} a special x",special_value == mid)

# # mid = 4 (no)
# right = mid
# mid = (left+right)//2
# print("Mid: ", mid)
# special_value = len(nums) - binarySearch(nums,mid)
# print("# elemnents: ",special_value) # > mid ==> increase mid
# print(f"Is {mid} a special x",special_value == mid)

# # mid = 3 (no)
# left = mid + 1 # 4 === right ==> break
# print("Array is not special ")

"""
l < r ---> l < m < r
l = m + 1 --> l <= r
l < r = m
m = (l+r) // 2 ----> m = l if l = r - 1 ----> l = m + 1 = r -----> break ----> return m + 1 with nums[m] < target
"""


# 704. Binary Search (%92)
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2 # Index
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
            
        return -1



class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right)//2 # Index

            # print(f"Value: {nums[mid]}, Mid: {mid}, Left: {left}, Right: {right}")
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid
            else: # reduce redundant loops when target === right
                return mid
            
        return -1

# Special Array With X Elements Greater Than or Equal X
# 1
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            x = len(nums) - m
            if nums[m] >= x:
                if m == 0 or nums[m - 1] < x:
                    return x
                else:
                    r = m - 1
            else:
                l = m + 1
        return -1
# 2
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left+right)//2
            special_value = len(nums) - self.binarySearch(nums,mid)
            print(f"Is {mid} a special value: {special_value}",special_value == mid)
            if special_value > mid:
                left = mid + 1
            elif special_value < mid:
                right = mid
            else:
                return mid
        else:
            mid = (left+right)//2
            special_value = len(nums) - self.binarySearch(nums,mid)
            if special_value == mid:
                return mid
       
        return -1
    
    def binarySearch(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r: 
            m = (l+r)//2 
            if nums[m] < target:
                l = m + 1 
            else:
                r = m
        return l
