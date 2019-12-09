# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val #since, there is no reference for the previous node.we can't modify the pointer of previous node.
        #Instead, we can copy the value of next node and paste it to the current node(act as next node now) and delete the next node
        node.next=node.next.next
