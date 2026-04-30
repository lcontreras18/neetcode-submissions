class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {}
        t_frequency = {}

        for char in s:
            s_frequency[char] = s_frequency.get(char, 0) + 1
        
        for char in t:
            t_frequency[char] = t_frequency.get(char, 0) + 1

        return s_frequency == t_frequency