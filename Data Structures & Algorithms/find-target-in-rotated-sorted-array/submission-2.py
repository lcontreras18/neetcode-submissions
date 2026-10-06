class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        min_index = right

        if min_index == 0:
            left = 0
            right = n - 1
        elif nums[0] <= target <= nums[min_index - 1]:
            left = 0
            right = min_index - 1
        else:
            left = min_index
            right = n - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1
        
