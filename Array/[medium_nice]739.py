# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n   =   len(temperatures)
        answer = [0]*n
        hottest = 0

        for index in range(n-1,-1,-1):
            if temperatures[index] >= hottest:
                hottest = temperatures[index]
                continue
            
            days = 1
            while temperatures[index] >= temperatures[index + days]:
                days += answer[index +days]
            answer[index] = days
        return answer
