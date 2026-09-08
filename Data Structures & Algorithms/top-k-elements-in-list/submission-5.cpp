class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> buckets(nums.size() + 1);

        unordered_map<int, int> freq;

        for(int n : nums) {
            freq[n]++;
        }

        for(auto& pair: freq) {
            int num = pair.first;
            int count = pair.second;
            
            buckets[count].push_back(num);
        }

        vector<int> result;
        for (int i = buckets.size() - 1; i >= 0; i--) {
            for(int j = 0; j < buckets[i].size(); j++) {
                result.push_back(buckets[i][j]);
                if(result.size() == k) {
                    return result;
                }
            }

        }

    }
};
