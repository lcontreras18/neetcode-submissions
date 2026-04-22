class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for(int value: nums){
            if(seen.contains(value)){
                return true;
            }
            else{
                seen.insert(value);
            }

        }
        return false;
    }
};