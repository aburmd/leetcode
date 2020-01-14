"""Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        while n!=1:
            res=int(n%3)
            if res!=0:
                return False
            else:
                n=int(n/3)
        return True

"""
FirstCommit: 
Runtime: 96 ms, faster than 17.32% of Python3 online submissions for Power of Three.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Three.
"""