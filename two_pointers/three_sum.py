class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        LeetCode 15: 3Sum
        Pattern: Two Pointers
        Difficulty: Medium
        Link: https://leetcode.com/problems/3sum/description/
        '''
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result
    
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # Example usage