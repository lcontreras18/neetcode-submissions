class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int right = 0;
        int best = 0;

        unordered_map<char, int>frequency;

        while (right < s.size()) {
            frequency[s[right]] += 1;
            int max_frequency = max(max_frequency, frequency[s[right]]);

            while(((right - left +1) - max_frequency) > k) {
                frequency[s[left]] -= 1;
                left += 1;
            }
            best = max(best, right - left + 1);
            right += 1;
            


        }
        return best;
        
        
    }
};
