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


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dict_s={}
        dict_t={}
        for i in s:
            if i not in dict_s:
                dict_s[i]=1
            else:
                dict_s[i]+=1
        for j in t:
            if j not in dict_s.keys():
                return False
            else:
                dict_s[j]-=1
                if dict_s[j]==-1:
                    return False
        return True
