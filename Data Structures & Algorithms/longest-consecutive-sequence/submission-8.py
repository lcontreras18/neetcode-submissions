class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        seen = set(nums)

        for num in nums:
            if num - 1 in seen:
                continue
            else:
                current = 1
                while num + 1 in seen:
                    current += 1
                    num += 1
            best = max(best, current)

        return best
