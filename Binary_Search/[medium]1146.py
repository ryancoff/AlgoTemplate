# 1146. Snapshot Array ()
# Binary Search 
# [snap_id, val]
class SnapshotArray(object):

    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in xrange(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

# (94.27%)
class SnapshotArray:

    def __init__(self, length: int):
        self.values_arr = [[0] for x in range(length)]
        # print("Init values_arr: \n",self.values_arr)
        self.total_snap = 0

    def set(self, index: int, val: int) -> None:
        idx_length = len(self.values_arr[index])
        if (idx_length == self.total_snap + 1):
            self.values_arr[index].pop(-1)
        else:
            last_val = self.values_arr[index][-1]
            self.values_arr[index].extend([last_val]*(self.total_snap-idx_length))
        self.values_arr[index].append(val)
        # self.values_arr[index].append(val)
        
    def snap(self) -> int:
        self.total_snap += 1
        return self.total_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        # print(f"{snap_id} --- current values_arr: \n: ",self.values_arr)
        # print(f"{index}: ",self.values_arr[index])
        id_index = min(snap_id, len(self.values_arr[index])-1)
        # print(id_index)
        # print(f"{index}: ",self.values_arr[index])
        return self.values_arr[index][id_index]
    