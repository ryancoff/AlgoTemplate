# 528. Random Pick with Weight (87.33%)
import random

class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sums = []
        prefix_sum=0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sums)
        while left < right:
            mid = left + (right-left)//2
            # prefix_sums is non-decreasing array
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# w[] = {2,5,3,4} => wsum[] = {2,7,10,14}
# w[] = {1,5,1,1,1} => wsum[] = {1,6,7,8,9}
# w[] = {1,2,3,4,5} => wsum[] = {1,3,6,10,15}
# target in [0,9] 
# find target in prefix_sums
# ---> % in 5 ---> find target ---> 11,12,13,14,15
# ---> % in 4 ---> find target ---> 7,8,9,10
# ---> % in 3 ---> find target ---> 4,5,6
# ---> % in 2 ---> find target ---> 2,3
# ---> % in 1 ---> find target ---> 1

# target = [0,1,2,3,4,5,6,7,8,9]