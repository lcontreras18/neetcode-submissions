class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1 
            else:
                matches += 0
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            rIndex = ord(s2[right]) - ord('a')
            s2Count[rIndex] += 1 
            if s2Count[rIndex] == s1Count[rIndex]:
                matches +=1
            elif s1Count[rIndex] + 1 == s2Count[rIndex]:
                matches -= 1 
            
            lIndex = ord(s2[left]) - ord('a')
            s2Count[lIndex] -= 1 
            if s2Count[lIndex] == s1Count[lIndex]:
                matches +=1
            elif s1Count[lIndex] - 1 == s2Count[lIndex]:
                matches -= 1 
            left += 1
        
        return matches == 26


