class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[]for i in range (len(nums)+ 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, freq in freq.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res