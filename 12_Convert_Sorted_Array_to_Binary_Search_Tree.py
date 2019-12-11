
"""Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Your input
[-10,-3,0,5,9]
Output
[0,-3,9,-10,null,5]
Expected
[0,-3,9,-10,null,5]"""


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.nodelist=[]
	def splitArray(self, nums):
		mid_element_index=len(nums)/2
		mid_element=nums[mid_element_index]
		firstHalf=nums[:mid_element_index]
		secondHalf=nums[mid_element_index+1:]
		return [mid_element,firstHalf,secondHalf]
	def insertNode(self, nums):
		#print nums
		if not (nums[1] or nums[2]):
			x=TreeNode(nums[0])
			self.nodelist.append(x.val)
			return x
		elif not nums[1]:
			rightchild=self.insertNode(self.splitArray(nums[2]))
			leftchild=None
		elif not nums[2]:
			leftchild=self.insertNode(self.splitArray(nums[1]))
			rightchild=None
		else:
			rightchild=self.insertNode(self.splitArray(nums[2]))
			leftchild=self.insertNode(self.splitArray(nums[1]))
		x=TreeNode(nums[0])
		self.nodelist.append(x.val)
		x.left=leftchild
		x.right=rightchild
		return x
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if nums:
			return self.insertNode(self.splitArray(nums))
		#return self.nodeTraverse()
	def nodeTraverse(self):
		return self.nodelist
