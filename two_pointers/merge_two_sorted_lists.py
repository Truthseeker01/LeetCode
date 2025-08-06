class Solution:
    
    def mergeTwoLists(self, list1, list2):
        '''
        LeetCode 21: Merge Two Sorted Lists
        Pattern: Two Pointers
        Difficulty: Easy
        Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
        '''
        h1 = list1
        h2 = list2
        dummy = ListNode(0)
        curr = dummy
        
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        curr.next = h1 if h1 else h2
        return dummy.next