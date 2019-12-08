class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        z=''
        j=len(s)
        for i in range(0,len(s)):
            if not(j<=i):
                z=s[i]
                s[i]=s[j-1]
                s[j-1]=z
                j=len(s)-(i+1)
        return s
