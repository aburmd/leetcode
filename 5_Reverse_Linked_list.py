# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node=None
        curr_node=head
        while curr_node:
            next_node=curr_node.next #prev_node=None curr_node=1 next_node=2 ,                     #prev_node=1 curr_node=2 next_node=3 
            #Remember next node
            curr_node.next=prev_node #prev_node=None curr_node=1 next_node=2 curr_node.next=None , #prev_node=1 curr_node=2 next_node=3 curr_node.next=1
            # REVERSE! None, first time round
            prev_node=curr_node      #prev_node=1 curr_node=1 next_node=2 curr_node.next=None ,    #prev_node=2 curr_node=2 next_node=3 curr_node.next=1
            # Used in the next iteration
            curr_node = next_node    #prev_node=1 curr_node=2 next_node=2 curr_node.next=None ,    #prev_node=2 curr_node=3 next_node=3 curr_node.next=1
            # Move to next node
        head=prev_node
        return head
