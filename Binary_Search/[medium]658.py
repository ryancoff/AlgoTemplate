# 658. Find K Closest Elements (91.52%)
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right-left)//2
            if x > arr[mid]:
                left = mid + 1
            else:
                right = mid
                
        print("pos: ",left)
        # arr[left-k:left+k]
        queue = []
        for index in range(-1*k,k+1): # In case x not belong to arr
            if (0 <= left + index ) and (left + index < len(arr)):
                if len(queue) < k:
                    queue.append(arr[left+index])
                else:
                    # print(f"{queue}--{arr[left+index]} -- pos: {left+index}")
                    if self.isBsmaller(queue[0],arr[left+index],x):
                        queue.pop(0) # Be careful
                        queue.append(arr[left+index])
                    # elif self.compare(queue[-1],arr[left+index],x):
                        
        return queue
    
    def isBsmaller(self,a,b,x):
        if abs(a-x) < abs(b-x):
            return False # a
        elif (abs(a-x) == abs(b-x)) and a < b:
            return False # a
        else:
            return True # b
                
        