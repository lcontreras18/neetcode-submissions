import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) >= 2:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(heap, stone1 - stone2)


        return 0 if len(heap) == 0 else -heap[0]