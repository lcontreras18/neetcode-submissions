class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());        
        int best = right;

        while (left <= right) {
            int hours = 0;
            int mid = (right + left) / 2;

            for(int pile: piles) {
                hours += (pile + mid - 1) / mid;
            } 

            if(hours > h) {
                left = mid + 1;
            } else {
                best = min(best,mid);
                right = mid - 1;
            }
        }
        
        return best;
    }
};
