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




#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
