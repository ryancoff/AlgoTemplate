# 1712. Ways to Split Array Into Three Subarrays (92.16%)

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = 0
        for i in range(1, len(nums)): 
            j = bisect_left(prefix, 2*prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1])//2)
            ans += max(0, min(len(nums), k) - max(i+1, j))
        return ans % 1_000_000_007

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        prefix_sum = 0
        prefix_sums = [0]
        ret = 0

        for num in nums:
            # prefix_sum += num
            prefix_sums.append(prefix_sums[-1]+num)

        # print("prefix_sums: ", prefix_sums)
        # print("total: ", prefix_sum)
        lo, hi = 0, 1
        idx_left, idx_right = 0, 0
        mid_point = (prefix_sums[0]+prefix_sums[-1])//2

        # while 2*prefix_sums[lo] <= (prefix_sums[lo]+prefix_sums[-1])//2 and prefix_sums[lo+1] < prefix_sums[-1] :
        for lo in range(1,len(nums)):
            if 2*prefix_sums[lo] > (prefix_sums[lo]+prefix_sums[-1])//2:
                continue
            lowerBound = 2*prefix_sums[lo]
            upperBound = (prefix_sums[lo]+prefix_sums[-1])//2


            # idx_left = bisect.bisect_left(prefix_sums[lo+1:], lowerBound) # >= lowerBound
            # idx_right = bisect.bisect_right(prefix_sums[lo+1:], upperBound) - 1  # [:idx_right] <= upperBound
            # F**g Slow??

            # idx_left = bisect.bisect_left(prefix_sums, lowerBound) # >= lowerBound
            # idx_right = bisect.bisect_right(prefix_sums, upperBound) - 1  # [:idx_right] <= upperBound
            # ret += idx_right - idx_left + 1
            # Missing Cases

            # idx_left = bisect.bisect_left(prefix_sums, lowerBound) # >= lowerBound                                  
            # idx_right = bisect.bisect_right(prefix_sums, upperBound)  # [:idx_right] <= upperBound
            idx_left = bisect.bisect_left(prefix_sums, lowerBound) # >= lowerBound
            idx_right = bisect.bisect_right(prefix_sums, upperBound)  # [:idx_right] <= upperBound
            ret += max(0, min(len(nums), idx_right) - max(lo+1, idx_left))

            # lo += 1



        return ret % 1_000_000_007

    def binarySearchRight(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    def binarySearchLeft(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left



"""
lo: ps[lo] = left <= mid = ps[hi] - ps[lo]
lo: ps[lo]*2 <= ps[hi] 

hi: ps[hi] - ps[lo] = mid <= ps[-1]//2

[1, 3, 5, 7, 12, 12]
lo: 1 1 1
hi: 3 5 7 (7-1=6) (12-7=5)  (hi-lo) > (ps[-1]-hi) --break

binarySearch ---> left=1, right = 12 --> mid = 6 --> hi - 1 <= 12 - hi ---> hi <= (12+1)//2  

2*ps[lo] <= ps[hi] <= mid

2 <= ... <= 6 --> [1] [3,5]

lo: 3           3                            3
hi: 5 (5-3=2<3) 7 (3<7-3=4) (4<12-7=5)       12(==ps[-1]) (12-3) > (12-12)

lowerBound binarySearch: lo: 3 --> 6 <= ps[hi] 
binarySearch --> left=3 , right = 12 --> mid = 7 --> found

2*ps[lo] <= ps[hi] <= mid ---> 7 (prefix_sums space)

6 <= ... <= 7 --> [3] [7]

lo: 5
hi: 7 (7-5=2<5)



lowerBound binarySearch: lo:5 --> 10 <= ps[hi] 
upperBound binarySearch --> left=5, right = 12 --> mid = 8 

2*ps[lo] <= ps[hi] <= mid ---> empty 

10 <= ... <= 8 ---> break

lo: 7
hi: 12 (==ps[-1]) -- break

lo: 12 (==ps[-1]) -- break

14 <= ... <= 9

ps[hi] + ps[lo] >  2*ps[lo] > (ps[-1] = ps[right]-ps[hi] + ps[hi] - ps[lo] + ps[lo]) + ps[0] = ps[right] + ps[0]

0 > ps[right] + ps[0]
"""