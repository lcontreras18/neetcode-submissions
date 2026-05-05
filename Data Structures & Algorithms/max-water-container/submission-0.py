class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        best = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if area > best:
                best = area
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return best 