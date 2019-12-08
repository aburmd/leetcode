class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remaining_val=0
        x=''
        y=''
        for i in range(0,len(nums)-1):
            remaining_val=target-nums[i]
            for j in range(i+1,len(nums)):
                if remaining_val==nums[j]:
                    x=i
                    y=j
        return [x,y]

    def twoSum1(self, nums, target):
        key=range(0,len(nums))
        nums_dict=dict(zip(nums,key))
        for i in key:
            remaining_val=target-nums[i]
            if remaining_val in nums[0:i] or remaining_val in nums[i+1:len(nums)]:
                return [i,nums_dict[remaining_val]]
## More Effcient
    def twoSum2(self,nums, target):
        dct={}
        for i in range(0,len(nums)):
            if target-nums[i] not in dct:
                dct[nums[i]]=i
            else:
                return [i,dct[target-nums[i]]]

    def twoSum3(self, nums, target):
        nums_dict={}
        for key,value in enumerate(nums):
            remaining=target-value
            if remaining in nums_dict:
                return [key,nums_dict[remaining]]
            nums_dict[value]=key
        return []
X
