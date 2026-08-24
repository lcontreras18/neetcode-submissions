class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0 
        best = 0
        counts = {}
        
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_frequency = max(counts.values())

            while((right - left + 1) - max_frequency > k):
                counts[s[left]] = counts.get(s[left],0) - 1
                left += 1
            
            best = max(best, right - left + 1)
    
        return best
