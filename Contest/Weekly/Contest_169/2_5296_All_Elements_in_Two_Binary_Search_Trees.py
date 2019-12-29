"""Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LinkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.cur1Node=None
        self.cur2Node=None
    def traverse1(self,root1):
        if root1:
            return self.traverseinOrder1(root1)
    def traverseinOrder1(self,root1):
        if root1.right:
            self.traverseinOrder1(root1.right)
        if self.cur1Node:
            preNode=self.cur1Node
            self.cur1Node=LinkedNode(root1.val)
            self.cur1Node.next=preNode
        else:
            self.cur1Node=LinkedNode(root1.val)
        if root1.left:
            self.traverseinOrder1(root1.left)
    def traverse2(self,root2):
        if root2:
            return self.traverseinOrder2(root2)
    def traverseinOrder2(self,root2):
        if root2.right:
            self.traverseinOrder2(root2.right)
        if self.cur2Node:
            preNode=self.cur2Node
            self.cur2Node=LinkedNode(root2.val)
            self.cur2Node.next=preNode
        else:
            self.cur2Node=LinkedNode(root2.val)
        if root2.left:
            self.traverseinOrder2(root2.left)
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.traverse1(root1)
        self.traverse2(root2)
        x=self.mergeTwoLists(self.cur1Node,self.cur2Node)
        y=[]
        while x:
            y.append(x.val)
            x=x.next
        return y


"""
First Commit:
Contest: Completed within that timeframe. Solution provides a correct output, but, lengthy approach.
BST --> sorted linked list (1 & 2) --> Sorted Array
"""
