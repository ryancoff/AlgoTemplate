# 1658. Minimum Operations to Reduce X to Zero (91.15% )

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = 0
        current = 0

        for right in range(n):
            # sum([left ,..., right]) = total - x
            current += nums[right]
            # if larger, move `left` to left
            while current > total-x and left <= right:
                current -= nums[left]
                left += 1
            # check if equal
            if current == total-x:
                maxi = max(maxi, right-left+1)

        return n-maxi if maxi != -1 else -1