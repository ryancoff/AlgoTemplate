# 826. Most Profit Assigning Work

# Two pointers (96.96%)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        '''
        Time: O(N log(N) + M log(M)) where N = len(diffiulty) and M = len(worker)
        Space: O(N)
        '''
        # Initialization
        jobs = sorted(zip(difficulty, profit))
        jobs_len = len(jobs)
        i, totalProfit, maxProfit = 0, 0, 0
        
        # Find max profit by checking it for all workers
        for effort in sorted(worker):
            
            # Find maximum profit that can be raked in with this effort
            while i < jobs_len and jobs[i][0] <= effort:
                maxProfit = max(maxProfit, jobs[i][1])
                i += 1
            
            # Update totalProfit. If i == jobs_len, it will keep adding last maxProfit for remaining workers
            totalProfit += maxProfit
            
        return totalProfit
        
            
        
        
# BinarySearch
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        earning = sorted(zip(difficulty,profit))
        earning_wo_diff = [x[1] for x in earning]
        max_profit = 0
        for w in worker:
            idx = self.alterbinarySearchRight(earning,w)
            if earning[idx][0] <= w:
                temp = max(earning_wo_diff[:idx+1])
                # print(f"idx: {idx} & temp: {temp}")
                max_profit += temp
            # else: # idx == 0

        return max_profit
    
    def alterbinarySearchRight(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2

            if nums[mid][0] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left - 1 if left else 0 # a[:left] <= target

difficulty = [68,35,52,47,86]
profit = [67,17,1,81,3]

values = sorted(zip(difficulty,profit))
earning_wo_diff = [x[1] for x in values]
print(values)
print(earning_wo_diff[:3])
print(max(earning_wo_diff[:3]))
import bisect

print(bisect.bisect([47,57,85],40))