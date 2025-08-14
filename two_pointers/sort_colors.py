class Solution(object):
    def sortColors(self, nums):
        """
        LeetCode 75: Sort Colors
        Pattern: Two Pointers
        Difficulty: Medium
        Link: https://leetcode.com/problems/sort-colors/description/
        """

        left, right = 0, len(nums) - 1
        current = 0
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1
        return nums
    
print(Solution().sortColors([2, 0, 2, 1, 1, 0]))  # Example usage