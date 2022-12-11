# 2271. Maximum White Tiles Covered by a Carpet (89.30%)

# Two pointer (98.52%)
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        res = 0
        l, r = 0, 0
        N = len(tiles)
        cover = 0
        while res < carpetLen and r < N:
            if tiles[l][0] + carpetLen > tiles[r][1]:
                cover += tiles[r][1] - tiles[r][0] + 1
                res = max(res, cover)
                r += 1
            else:
                partial = max(0, tiles[l][0] + carpetLen - tiles[r][0])
                res = max(res, cover + partial)
                cover -= tiles[l][1] - tiles[l][0] + 1
                l += 1
        
        return res


# Binary Seach 
import bisect
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], l: int) -> int:
        pref_sum = [0]
        start_pos = []
        sol = 0
        tiles.sort()
        for start, end in tiles:
            pref_sum.append(end - start + 1 + pref_sum[-1])
            start_pos.append(start)
        # print("pref_sum: ",pref_sum)
        for i, (x, y) in enumerate(tiles):
            tar = x + l - 1
            # print(f"x: {x} - l: {l} - i: {i}")
            near = bisect.bisect_right(start_pos, tar, lo=i) - 1
            # [1, 10, 12, 20, 30]

            left = pref_sum[near] - pref_sum[i]
            # [0, 5, 7, 14, 20, 23]
            right = 0
            if near < len(start_pos):
                right = min((tar - start_pos[near] + 1) * int(tar - start_pos[near] >= 0),
                            tiles[near][1] - tiles[near][0] + 1)
            sol = max(sol, left + right)
            # print(f"tar: {tar} - near: {near} - left: {left} - right: {right} - sol: {sol}")
            # print("\n")
        return sol
