# 729. My Calendar I (97.85%)
# 2
class MyCalendar:

    def __init__(self):
        self.calendar = [(0,0),(1e9,1e9)] # Reduce to only middle case
    def book(self, start: int, end: int) -> bool:
        l,r = 0,len(self.calendar)
        while l<r:
            mid = (l+r)//2
            if end <= self.calendar[mid][0]:
                r = mid
            else:
                l=mid+1
        if self.calendar[l-1][1] > start: 
            return False
        self.calendar.insert(l,(start,end))
        return True

#1
class MyCalendar:

    def __init__(self):
        self.meeting = []
        

    def book(self, start: int, end: int) -> bool:
        # print(f"Entry: {start} - {end}", )
        # print("Check-in: ",self.meeting)
        if len(self.meeting) == 0:
            self.meeting.append([start,end])
            return True
        elif end > self.meeting[-1][1]:
            # print("Here 1!")
            pos_o_start = self.binarySearch(self.meeting[-1],start)
            if pos_o_start == len(self.meeting[-1]):
                self.meeting.append([start,end])
                return True
            elif pos_o_start + 1 == len(self.meeting[-1]) and self.meeting[-1][1] == start:
                self.meeting.append([start,end])
                return True
            else:
                return False
            
        elif start < self.meeting[0][0]:
            # print("Here 2!")
            pos_o_end = self.binarySearch(self.meeting[0],end)
            if pos_o_end == 0:
                temp = []
                temp.append([start,end])
                temp.extend(self.meeting)
                self.meeting = temp
                return True
            else:
                return False
        else:
            temp_list = list(zip(*self.meeting))
            # print("Here 3!: ",temp_list[0]) # First element of each entry
            pos = self.binarySearch(temp_list[0],start) # First element of each entry
            # print("Position: ",pos)
            if self.meeting[pos-1][1] <= start and end <= self.meeting[pos][0]:
                temp = []
                temp.extend(self.meeting[:pos])
                temp.append([start,end])
                temp.extend(self.meeting[pos:])
                self.meeting=temp
                return True
            else:
                return False
            
            
            
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (right+left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left