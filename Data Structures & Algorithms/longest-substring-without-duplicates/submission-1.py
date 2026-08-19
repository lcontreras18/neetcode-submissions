class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        left = 0
        right = 0 

        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
            seen.add(s[right])
            right += 1
            best = max(best, right - left)
        
        return best
