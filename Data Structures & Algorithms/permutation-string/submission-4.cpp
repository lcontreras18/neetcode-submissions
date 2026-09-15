class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size()) {
            return false;
        }
        
        int left = 0;
        int right = 0;
        
        unordered_map<char,int>s1_count;

        for(char c: s1) {
            s1_count[c] += 1;
        }
        
        unordered_map<char,int>s2_count;
        while(right < s2.size()) {
            s2_count[s2[right]] += 1;

            if(right - left + 1 > s1.size()) {
                s2_count[s2[left]] -= 1;
                if(s2_count[s2[left]] == 0) {
                    s2_count.erase(s2[left]);
                }
                left += 1;
            }
            
            if( s1_count == s2_count) {
                return true;
            }

            right += 1;
        }
        return false;

    }
};
