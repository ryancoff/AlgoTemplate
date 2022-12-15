# 1574. Shortest Subarray to be Removed to Make Array Sorted 
# Good for divide and conquer
# separate cases

# 96.69%
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        minLength = int(1e9)
        if len(arr) == 1:
            return 0


        # Case 1 [1,2,3,4,5,2,4,1,0,6,5]
        # Case 2 [10,5,2,5,0,5,5,4,1,2,3,4,5,6]
        # Case 3 [1,2,3,10,0,4,1,6,3, 2,3,5] 
        # Case 3 [1,2,5,10,0,4,1,6,3, 2,3,5] 

        # Separately Left Pointer (Case 2) & Right Pointer (Case 3)

        
        # Case 2: Right off
        # if arr[left] > arr[left+1]
        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1

        # Case 3: In between
        # if arr[left] <= arr[left+1]:
        while left < right and  arr[left] <= arr[left+1]:
            left += 1

        # print(f"{left} & {right}")

        # Case 1:
        # if arr[left] >= arr[right]:
        if right == left:
            return 0
        elif right == len(arr) - 1 and left == 0:
            minLength = min(minLength,right-left-1) if arr[left] <= arr[right] else min(minLength,right-left)
        elif right == len(arr) - 1 or left == 0:
            minLength = min(minLength,right-left) 
        

        if left > 0 and arr[left-1] > arr[right]:
            print(f"{left} & {right}")
            temp_left = left
            temp_right = right
            while right < len(arr) and arr[left-1] > arr[right]:
                right += 1

            print(f"{left} & {right} {len(arr)}")
            # and arr[right] < arr[left-1]
            if  right < len(arr) and arr[left] < arr[right]:
                print(f"{arr[left-1]} {arr[left]} {arr[right]} {arr[right+1]}")
                minLength = min(minLength, right-left-1) # not remove left 
            else:
                minLength =min(minLength, right-left) if right < len(arr)  else min(minLength, right-1-left)

            left = temp_left
            right = temp_right
            while left > 0 and arr[left-1] > arr[right]:
                left -= 1
            minLength =min(minLength, right-left)
        else:
            print(f"{left} & {right}")
            minLength =min(minLength, right-left) if arr[right] < arr[left] else min(minLength, right-left-1)

        

            


        # # Case 3: Somewhere in middle
        # while arr[right-1] <= arr[Right]:
        #     right -= 1
        #     pass

        return minLength
    
"""
The answer is formed from the beginning and we discard all the elements after the first decreasing element we find.
The answer is formed from the end, i.e, we get an increasing sequence once we delete some numbers from the front.
The answer is formed by removing some elements from the middle.
"""