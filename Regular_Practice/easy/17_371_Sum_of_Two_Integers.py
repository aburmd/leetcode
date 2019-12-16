"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""

class Solution:
    def getPositiveIntegerSum(self,a,b):
        while b!=0:
            bitcommon=a&b
            a=a^b #bitdiff assign back to a
            b=bitcommon<<1 #push one bit to adjust the value
        return a

    def getNegativeIntegerSum(self,a,b):
        upperbound=0xfffffffff
        upperbound_plus1=self.getPositiveIntegerSum(upperbound,1)
        b=b&0xfffffffff
        a=self.getPositiveIntegerSum(a,b)
        if a>=upperbound:
            return -1 if a%upperbound==0 else a%upperbound_plus1
        else:
            print("2",a,upperbound_plus1)
            return -1*((-1*(a%upperbound))&0xfffffffff)

    def getSum(self,a, b):
        if a==-b:
            return 0
        if a>=0 and b>=0:
            return self.getPositiveIntegerSum(a,b)
        else:
            if b<=0 and a<=0:
                b=-1*b
                a=-1*a
                x=self.getSum(a,b)
                return -1*x
            elif b<0:
                return self.getNegativeIntegerSum(a,b)
            elif a<0:
                return self.getNegativeIntegerSum(b,a)


"""
FirstCommit:
Runtime: 24 ms, faster than 92.83% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sum of Two Integers.
"""

