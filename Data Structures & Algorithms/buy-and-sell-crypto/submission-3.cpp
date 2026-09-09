class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 1;
        int best = 0;

        while (right < prices.size()) {
            if (prices[left] > prices[right]) {
                left = right;
                right += 1;
            }   else {
                best = max(best,prices[right] - prices[left]);
                right += 1;
            }
        }
        return best;
    }
};
