import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = math.sqrt((point[0]**2) + (point[1]**2))

            heapq.heappush(heap, (distance, point))
        
        res = []

        for i in range(k):
            value = heapq.heappop(heap)

            res.append(value[1])

        return res




