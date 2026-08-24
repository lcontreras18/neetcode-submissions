class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for char in s1:
            count1[ord(char) - ord('a')] += 1 
        
        left = 0

        for right in range(len(s2)):
            count2[ord(s2[right]) - ord('a')] += 1 
            
            window_size = right - left + 1
            if window_size > len(s1):
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1 

            if count2 == count1:
                return True

        return False
