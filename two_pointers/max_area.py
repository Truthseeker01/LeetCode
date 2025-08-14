class Solution(object):
    def maxArea(self, height):
        """
        LeetCode 11: Container With Most Water
        Pattern: Two Pointers
        Difficulty: Medium
        Link: https://leetcode.com/problems/container-with-most-water/description/
        """
        left, right = 0, len(height) - 1
        a = 0
        while left < right:
            if height[left] <= height[right]:
                if ((height[left]) * (right - left)) > a:
                    a = (height[left]) * (right - left)
                left += 1
            else:
                if ((height[right]) * (right - left)) > a:
                    a = (height[right]) * (right - left)
                right -= 1
        return a
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Example usage