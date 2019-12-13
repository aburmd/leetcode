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
        dct={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        for i in s[::-1]:
            power+=1
            multiplier=dct[i]
            columnNumber+=multiplier*self.powof26(power)
        return columnNumber

"""

Runtime: 32 ms, faster than 80.96% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

"""

