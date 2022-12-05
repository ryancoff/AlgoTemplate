# 74. Search a 2D Matrix (86.05%)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m,n = len(matrix), len(matrix[0])
        # print(f"{m}x{n}")
    
        for nums in matrix:
            left, right = 0, len(nums) - 1

            while left < right:

                mid = left + (right-left)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            if nums[left] == target:
                return True

        return False