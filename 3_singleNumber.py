class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct={}
        for key,value in enumerate(nums):
            if not (value in dct):
                dct[value]=key
            else:
                dct.pop(value)
        return nums[dct.values()[0]]
