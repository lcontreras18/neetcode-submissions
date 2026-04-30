class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_count = 0 
        
        for num in nums:
            if num-1 in nums:
                continue
            else:
                count = 1
                while num + count in nums:
                    count = count + 1
                if count > longest_count:
                    longest_count = count
        
        return longest_count
