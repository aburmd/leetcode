"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6


Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ln=len(arr)
        dct={}
        if ln==0:
            return None
        elif ln==1:
            return arr[0]

        for i in arr:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
            if dct[i]>ln//4:
                return i
        return None

"""
Solved within the contest
"""