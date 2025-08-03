import math

class Solution:
    def findSmallestMaxDist(self, stations, k):
        l = 0
        h = max(stations[i] - stations[i - 1] for i in range(1, len(stations)))
        eps = 1e-6  # Precision for floating point binary search

        while h - l > eps:
            mid = (l + h) / 2
            if self.is_possible(stations, mid, k):
                h = mid  # Try to minimize the max distance
            else:
                l = mid  # Need larger max distance

        return round(h, 2)

    def is_possible(self, stations, max_dis, k):
        cnt = 0
        for i in range(1, len(stations)):
            dis = stations[i] - stations[i - 1]
            # Number of additional stations needed in this segment
            cnt += math.ceil(dis / max_dis) - 1
        return cnt <= k
