# 739. Daily Temperatures (90%)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        # for i, temp in enumerate(temperatures):
            # if len(stack) == 0:
            #     stack.append((i,temp))
            # else:
            #     while stack and temp > stack[-1][1]:
            #         answer[stack[-1][0]] = i - stack[-1][0]
            #         stack.pop(-1)
            #     else:
            #         stack.append((i,temp))
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer