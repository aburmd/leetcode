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
    def getPositivesum(self,a,b):
        while b!=0:
            bitcommon=a&b #Example: 4(100),5(101) bit common(a&b) is 4(100)
            a=a^b #Example: 4(100),5(101) bit diff(a^b) is 1(001)
            b=bitcommon<<1 #Example: one shift, 4 one shift (4(100)<<1) is 8(1000)
        return a
    def getNegativesum(self,apos,bneg):
        upperbound=0xfffffffff #f-1111 ie 0xf-15 define the max value for calculation
        upperbound_plus1=self.getPositivesum(upperbound,1)
        b=bneg&0xfffffffff #negative value starts in reverse order from upperbound
        #like (-1&0xf->15,-1&0xff->255) here -1&0xfffffffff = -1=68719476735)
        a=self.getPositivesum(apos,b)
        if a==upperbound:
            return -1
        elif a>upperbound:
            return a%upperbound_plus1
        else:
            return -1*((-1*a)&0xfffffffff)
    def getSum(self,a, b):
        if a==(-1)*b:
            return 0
        elif a>=0 and b>=0:
            return self.getPositivesum(a,b)
        elif a<=0 and b<=0:
            apos=-1*a
            bpos=-1*b
            return -1*self.getPositivesum(apos,bpos)
        else:
            if b<0:
                return self.getNegativesum(a,b)
            else:
                return self.getNegativesum(b,a)


"""
SecondCommit:
Runtime: 24 ms, faster than 91.03% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sum of Two Integers..
FirstCommit:
Runtime: 24 ms, faster than 92.83% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sum of Two Integers.
"""

