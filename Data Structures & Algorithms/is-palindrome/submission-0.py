class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            
            start = start + 1
            end = end - 1
        
        return True