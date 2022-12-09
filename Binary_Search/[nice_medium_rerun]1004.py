# 1004. Max Consecutive Ones III (75%)

# Sliding Windows (98.88%)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1

# Binary Search + Prefix_sum (75%)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sums = []
        for num in nums:
            prefix_sum += num
            prefix_sums.append(prefix_sum)
        # print("Prefix_sums: ",prefix_sums)

        left, right = 0, len(nums)
        mid = 0
        while left < right:
            mid = left + (right-left)//2
            if self.checkLength(prefix_sums, mid, k): 
                left = mid + 1
            else:
                right = mid

        if self.checkLength(prefix_sums, left, k):
            # print("Hello!!")
            return left
        else:
            return left -1
        # return left
    
    def checkLength(self, prefix_sums, length, k) -> bool:
        if prefix_sums[length-1] + k >= length: # i =0
            return True

        for i in range(1,len(prefix_sums) - length + 1):
            if prefix_sums[length+i-1] - prefix_sums[i-1] + k >= length:
                return True
        return False