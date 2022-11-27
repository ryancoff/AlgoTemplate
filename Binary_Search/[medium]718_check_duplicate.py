# 718. Maximum Length of Repeated Subarray  (92.93%)
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        def check(length):
            seen = set(tuple(nums1[i:i+length]) 
                       for i in range(len(nums1) - length + 1))
            return any(tuple(nums2[j:j+length]) in seen 
                       for j in range(len(nums2) - length + 1))
        low, high = 0, len(nums1)
        while low < high:
            mid = low + (high-low)//2
            if check(mid): # check whether subarray can be larger
                low = mid + 1 # Increase mid --> 
            else: # subarray need to be smaller
                high = mid
        else: # Check low==high
            if check(low):
                return low
        return low - 1 # since low = answer + 1