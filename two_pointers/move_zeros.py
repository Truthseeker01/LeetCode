class Solution:
    
    def moveZeros(self, nums: list[int]) -> None:
        '''
        LeetCode 283: Move Zeroes
        Pattern: Two Pointers
        Difficulty: Easy
        Link: https://leetcode.com/problems/move-zeroes/description/
        '''
        # Using two pointers to move non-zero elements to the front
        # left = 0
        # for right in range(len(nums)):
        #     if nums[right] != 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        # return nums
        
        
        # Using a single pointer to shift non-zero elements
        # and fill the rest with zeros
        # Avoids unnecessary swaps in the first approach
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        return nums