# 240. Search a 2D Matrix II (72.88%)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        lastColumnIdx = self.binarySearch(matrix[0], target)
        if matrix[0][lastColumnIdx] == target:
            return True
        else:
            for i in range(1,len(matrix)):
                lastColumnIdx = self.binarySearch(matrix[i][:lastColumnIdx+1], target)
                if matrix[i][lastColumnIdx] == target:
                    return True
        return False
        

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] < target:
                left = mid + 1

            else:
                right = mid
        
        return left