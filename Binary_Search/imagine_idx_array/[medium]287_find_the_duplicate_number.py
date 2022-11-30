#287. Find the Duplicate Number (73.67%)
# find_the_duplicate_number
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        length = len(nums) # n + 1
        # count 1 2 3 4 ... n
        left, right = 0, length
        while left < right:
            mid = left + (right-left)//2
            count = sum(num <= mid for num in nums)
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left

# Similar Problems
# 540
