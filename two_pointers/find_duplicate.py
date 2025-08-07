class Solution:

    def findDuplicate(self, nums: list[int]) -> int:
        '''
        LeetCode 287: Find the Duplicate
        Pattern: Two Pointers
        Difficulty: Medium
        Link: https://leetcode.com/problems/find-the-duplicate-number/
        '''
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

ins = Solution()
print(ins.findDuplicate([1,3,4,2,2]))
