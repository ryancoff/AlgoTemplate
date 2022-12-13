# 1428. Leftmost Column with at Least a One (91.49%)
# Approach 3: Start at Top Right, Move Only Left and Down

# Binary Search with INF constant
class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        nr_rows, nr_cols = mat.dimensions()
        
        def find(row):
            left, right = 0, nr_cols - 1
            answer = float("inf")
            while left <= right:
                mid = (left + right) // 2
                if mat.get(row, mid) == 1:
                    answer = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return answer
        
        min_col = float("inf")
        for row in range(nr_rows):
            min_col = min(min_col, find(row))
        return min_col if min_col != float("inf") else -1

# origin (91.49%)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        sizes = binaryMatrix.dimensions()
        self.rows, self.cols = sizes[0], sizes[1]
        # return  binaryMatrix.get(0,0)
        ret = -1
        for row in range(self.rows):
            idx = self.binarySearch(binaryMatrix,row,1)
            if binaryMatrix.get(row,idx) == 1:
                if ret == -1: 
                    ret = idx
                else:
                    ret = min(ret,idx)



        return ret

    def binarySearch(self, binaryMatrix, row, target):
        left, right = 0, self.cols - 1
        while left < right:
            mid = left + (right-left)//2
            if binaryMatrix.get(row,mid) < target:
                left = mid + 1
            else:
                right = mid
        
        return left