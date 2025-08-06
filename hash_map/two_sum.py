class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        LeetCode 1: Two Sum
        Pattern: Two Pointers / Hash Map
        Difficulty: Easy
        Link: https://leetcode.com/problems/two-sum/description/
        '''
        num_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_map:
                return [num_map[diff], i]
            num_map[n] = i
        return []