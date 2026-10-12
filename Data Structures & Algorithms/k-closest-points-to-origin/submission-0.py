import heapq 
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x1 = point[0]
            y1 = point[1]

            distance = sqrt((x1 - 0)**2 + (y1 - 0)**2)

            heapq.heappush(heap,(distance, point))
        
        res = []

        for i in range(k):
            value = heapq.heappop(heap)
            res.append(value[1])
        
        return res
            

        #smallest distance first min heap