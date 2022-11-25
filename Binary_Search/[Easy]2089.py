# 2089. Find Target Indices After Sorting Array (91.25%)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ret = []
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        for indice, value in enumerate(nums[left:]):
            if value == target:
                ret.append(left+indice)
            else:
                break
        return ret
                