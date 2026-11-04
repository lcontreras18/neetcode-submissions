class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)

        for word in strs:
            frequency = [0] * 26 
            for char in word:
                frequency[ord('a') - ord(char)] += 1 

            group[tuple(frequency)].append(word)

        return list(group.values())        
        