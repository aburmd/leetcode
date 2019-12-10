"""Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""



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
