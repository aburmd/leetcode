"""Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dct={}
        half=(len(nums)//2)
        for value in nums:
            if value not in dct.keys():
                dct[value]=1
            else:
                dct[value]+=1
                if dct[value]>half:
                    return value
        return None

"""
Second Commit:
Runtime: 192 ms, faster than 64.23% of Python3 online submissions for Majority Element.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Majority Element.
"""