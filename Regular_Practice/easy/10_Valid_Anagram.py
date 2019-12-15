"""Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dct={}
        for value in s:
            if value not in dct.keys():
                dct[value]=1
            else:
                dct[value]+=1
        for value in t:
            if value in dct.keys():
                dct[value]-=1
                if dct[value]<0:
                    return False
            else:
                return False
        return True

"""
Second Commit:
Runtime: 60 ms, faster than 44.10% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.1 MB, less than 96.88% of Python3 online submissions for Valid Anagram.
"""
