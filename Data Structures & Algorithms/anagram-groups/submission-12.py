class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for word in strs:
            frequency = [0] * 26 
            for char in word:
                frequency[ord('a') - ord(char)] += 1 

            groups[tuple(frequency)].append(word)

        return list(groups.values())        
        