"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=collections.Counter(s)
        for i in range(0,len(s)):
            if c[s[i]]==1:
                return i
        return -1


"""
SecondCommit:
Runtime: 88 ms, faster than 88.45% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
FirstCommit:
Runtime: 144 ms, faster than 33.70% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.

"""

