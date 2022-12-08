# 167. Two Sum II - Input Array Is Sorted
# Two Pointer + Binary Search (98.3%)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)
        ret = []
        while left < right:
            mid = left + (right - left)//2
            sum = numbers[left]+numbers[right]
            if sum == target:
                ret.append[left+1]
                ret.append[right+1]
            elif sum < target:
                left = mid + 1 if (numbers[mid] + numbers[right] < target) else left + 1
            else:
                right = mid if (numbers[left] + numbers[mid] > target) else right - 1

        return ret
# Two pointer
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:        
        lPoint, rPoint = 0, len(numbers)-1
        while (lPoint < rPoint):
            currentSum = numbers[lPoint] + numbers[rPoint]
            if currentSum > target:
                rPoint -= 1
            elif currentSum < target:
                lPoint += 1
            else:
                return [lPoint+1, rPoint+1]


# Binary Search (5.2%)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        if target <= 0:
            upperBoundIdx = self.binarySearch(numbers, 0)
        else:
            upperBoundIdx = self.binarySearch(numbers, target)
        # print("upperBoundIdx: ",upperBoundIdx)
        for index in range(upperBoundIdx+1):
            first_index = index
            second_number = target - numbers[index]
            if second_number != numbers[index]:
                second_index = self.binarySearch(numbers[:upperBoundIdx+1], second_number)
            else:
                second_index = index + 1 + self.binarySearch(numbers[index+1:upperBoundIdx+1], second_number)
            if numbers[second_index] == second_number:
                return [first_index+1, second_index+1]

        return []

    def binarySearch(self, nums, target):
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left 

