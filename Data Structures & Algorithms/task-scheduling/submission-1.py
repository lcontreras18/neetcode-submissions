import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}

        for task in tasks:
            frequency[task] = frequency.get(task, 0) + 1 

        heap = []

        for count in frequency.values():
            heapq.heappush(heap, -count)
        
        q = deque()
        time = 0
        
        while heap or q:
            time += 1 

            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count, time + n])
            
            if q:
                if time == q[0][1]:
                    heapq.heappush(heap, q.popleft()[0])
            
        
        return time
            

        