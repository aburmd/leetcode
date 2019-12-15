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
    def pow(self,multiple,power):
        storeval={}
        if power==0:
            return 1
        if power==1:
            return multiple
        else:
            if power not in storeval.keys():
                storeval[str(multiple)+'-'+str(power)]=multiple*self.pow(multiple,power-1)
                return storeval[str(multiple)+'-'+str(power)]
            else:
                return storeval[str(multiple)+'-'+str(power)]


    def titleToNumber(self, s: str) -> int:
        alphaDct={}
        alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        counter=0
        result=0
        for key,value in enumerate(alpha):
            alphaDct[value]=key+1
        for i in s[::-1]:
            result+=alphaDct[i]*self.pow(26,counter)
            counter+=1
        return result

"""
Third Commit:
Runtime: 32 ms, faster than 80.27% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

Second Commit:
Runtime: 28 ms, faster than 92.06% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

Fisrt Commit:
Runtime: 32 ms, faster than 80.96% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
"""
