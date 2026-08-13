class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums)+ 1)]
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
        
        for num, count in counts.items():
            buckets[count].append(num)

        res = []

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
