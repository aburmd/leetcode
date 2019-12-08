class Solution(object):
    #Using Recursive Method
	def reverseString(self,s): 
		        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
		def helper(right,left):
			if left > right:
				s[right],s[left]=s[left],s[right]
				right=right+1
				left=left-1
				helper(right,left)
		helper(0,len(s)-1)
		return s

	#more efficent
    def reverseString1(self, s):
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