class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int best = 0;

        unordered_set<int> seen(nums.begin(), nums.end());

        for (int num : nums) {
            if (seen.contains(num - 1)) {
                continue;
            } else {
                int current = 1;
                while (seen.contains(num + current)) {
                    current += 1;
                }
                best = max(best, current);
            }
        }
        return best;

    }
};
