"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def hasSymmetric(T1,T2):
            if not T1 and not T2:
                return True
            elif (T1 and not T2) or (not T1 and T2):
                return False
            elif T1.val==T2.val:
                if hasSymmetric(T1.left,T2.right) and hasSymmetric(T1.right,T2.left):
                    return True
            else:
                return False
        if not root:
            return True
        else:
            return hasSymmetric(root.left,root.right)

"""
First Commit: Need to solve more Node problems.. This one also can only be solved after checking the code.

Runtime: 32 ms, faster than 67.21% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
"""