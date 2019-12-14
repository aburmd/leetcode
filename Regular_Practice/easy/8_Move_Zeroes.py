"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(0,len(nums)):
            if nums[i-k]==0:
                rm=nums.pop(i-k)
                nums.append(rm)
                k+=1
        return nums
    # Different Approach: both yields same time and memory
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[non_zero_index],nums[i]=nums[i],nums[non_zero_index]
                non_zero_index+=1
        return nums
