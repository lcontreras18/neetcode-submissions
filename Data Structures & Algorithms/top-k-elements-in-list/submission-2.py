class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        frequency_map = {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        for num, frequency in frequency_map.items():
            buckets[frequency].append(num)
        
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

