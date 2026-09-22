class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1

                while(left < right):
                    total = nums[i] + nums[right] + nums[left]

                    if total == 0:
                        res.append([nums[i], nums[right], nums[left]])
                        right -= 1
                        left += 1

                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                            
                    elif total < 0:
                        left += 1
                    else:
                        right -= 1
            
        return res
                        
            