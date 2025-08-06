class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        LeetCode 1: Two Sum
        Pattern: Two Pointers / Hash Map
        Difficulty: Easy
        Link: https://leetcode.com/problems/two-sum/description/
        '''
        
        num_map = {}
        #
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_map:
                # If the difference is found in the map, return the indices
                # of the current number and the number that completes the target
                return [num_map[diff], i]
            # Store the index of the current number in the map
            # to use it for future comparisons
            num_map[n] = i
        return []