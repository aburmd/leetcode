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



class Solution:
    def reverseString(self,s):
        half=len(s)//2
        for i in range(0,half):
            s[i],s[len(s)-1-i]=s[len(s)-1-i],s[i]
        return s


"""
Runtime: 240 ms, faster than 5.77% of Python3 online submissions for Best Time to reverseString.
Memory Usage: 17.3 MB, less than 98.84% of Python3 online submissions for Best Time to reverseString.
"""