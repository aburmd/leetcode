
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
    def mergeTwoLists(self,L1,L2):
        if not L1:
            return L2
        elif not L2:
            return L1
        else:
            if L1.val > L2.val:
                L2.next=self.mergeTwoLists(L2.next,L1)
                return L2
            else:
                L1.next=self.mergeTwoLists(L1.next,L2)
                return L1


"""
Second Commit: Nothing much different than previous.But, looks cleaner and easy to read
Runtime: 32 ms, faster than 80.81% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

First Commit:
Runtime: 28 ms, faster than 97.91% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""
