"""Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution:
    def powof26(self,n):
        storeValue={}
        if n==0:
            return 1
        elif n==1:
            return 26
        else:
            if n not in storeValue.keys():
                storeValue[n]=26*self.powof26(n-1)
                return storeValue[n]
            else:
                return storeValue[n]
            
        
    def titleToNumber(self, s: str) -> int:
        multiplier=0
        power=-1
        columnNumber=0
        aplha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dct={}
        for key,value in enumerate(aplha):
            dct[value]=key+1
        for i in s[::-1]:
            power+=1
            multiplier=dct[i]
            columnNumber+=multiplier*self.powof26(power)
        return columnNumber

"""
Runtime: 28 ms, faster than 92.06% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

Previous Commit:
Runtime: 32 ms, faster than 80.96% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

"""
