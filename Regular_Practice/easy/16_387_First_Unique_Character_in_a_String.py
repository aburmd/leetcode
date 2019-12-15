"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        elif len(s)==1:
            return 0
        dct={}
        lst=[]
        for key,value in enumerate(s):
            if value not in dct.keys():
                dct[value]=key
            else:
                dct[value]=-1
        for value,key in list(dct.items()):
            if (key!=-1) and (key not in lst):
                lst.append(key)
        lst.sort()
        return -1 if not len(lst) else lst[0]


"""
FirstCommit:
Runtime: 144 ms, faster than 33.70% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.

"""

