
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self,l1,l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val > l2.val:
            firstNode=l2
            if l1 or l2.next:
                firstNode.next=self.mergeTwoLists(l1,l2.next)
            return firstNode
        else:
            firstNode=l1
            if l2 or l1.next:
                firstNode.next=self.mergeTwoLists(l2,l1.next)
            return firstNode


"""
First Commit:
Runtime: 28 ms, faster than 97.91% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""
