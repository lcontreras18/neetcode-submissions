class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int best = 0;

        while(left < right) {
            int area = (right - left) * min(heights[left], heights[right]);
            best = max(best, area);

            if (heights[left] > heights[right]) {
                right -= 1;
            } else {
                left += 1;
            }
        }
        return best;
        
    }
};
