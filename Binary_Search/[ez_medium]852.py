# 852. Peak Index in a Mountain Array (%92.22)
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right-left)//2
            if arr[mid-1] < arr[mid]:
                left = mid + 1
            else:
                right = mid
        return left - 1