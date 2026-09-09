class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0; 
        int best = 0;

        unordered_set<char>seen;

        while(right < s.size()) {
            seen.insert(s[right]);
            right+= 1;
            best = max(right - left, best);
            while(seen.count(s[right])) {
                seen.erase(s[left]);
                left += 1;
            }
        }
        return best;
        
    }
};
