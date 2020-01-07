"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=[0]*len(nums)
        res[0]=nums[0]
        for i in range(1,len(nums)):
            res[i]=max(nums[i],nums[i]+res[i-1]) #actually, it updates an array to maximize the sum amount using prior to this elements.
        #print (nums)
        #print (res) #provides point in time maximum value in an array.
        return max(res) #it provides the maximum subarray sum value.

"""
FirstCommit: 
Runtime: 64 ms, faster than 81.64% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.5 MB, less than 91.06% of Python3 online submissions for Maximum Subarray.
"""