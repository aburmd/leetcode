"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=collections.Counter(nums1)
        c2=collections.Counter(nums2)
        res=[]
        common=c1&c2
        for i in common:
            res+=[i]*common[i]
        return res



"""
Third Commit: Please refer the previous commit on this file for regular approach
Runtime: 44 ms, faster than 90.97% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.

Second Commit:
Runtime: 48 ms, faster than 80.18% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
"""
