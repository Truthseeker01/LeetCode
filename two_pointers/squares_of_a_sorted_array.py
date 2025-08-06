class Solution:
    
    def sortedSquares(self, nums: list[int]) -> list[int]:
        '''
        LeetCode 977: Squares of a Sorted Array
        Pattern: Two Pointers
        Difficulty: Easy
        Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/
        '''
        left, right = 0, len(nums) - 1
        squares = []
        while left <= right:
            #left_square = nums[left] ** 2
            #right_square = nums[right] ** 2
            # You can also simplify it with "if abs(nums[left]**2) > abs(nums[right]**2):" 
            # so you dont need to get the squares and compare them

            if abs(nums[left]**2) > abs(nums[right]**2):
                squares.append(nums[left] ** 2)
                left += 1
            else:
                squares.append(nums[right] ** 2)
                right -= 1
        # Reverse to get sorted order
        return squares[::-1]