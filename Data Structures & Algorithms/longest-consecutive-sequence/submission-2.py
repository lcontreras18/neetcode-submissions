class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0
        
        for num in nums:
            if num - 1 in numSet:
                continue
            else:
                current = 1
                while num + 1 in numSet:
                    num += 1
                    current += 1
                best = max(best,current)
        return best
        