"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"


Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha='0abcdefghijklmnopqrstuvwxyz'
        res=''
        dct={}
        x=0
        for i,j in enumerate(alpha):
            if i>9:
                dct[str(i)+'#']=j
            else:
                dct[str(i)]=j
        arrseq=[]
        for i in range(0,len(s)):
            if s[i]=='#':
                #print('1',arrseq[-1])
                arrseq.pop()
                #print(arrseq)
                #print('2',arrseq[-1])
                arrseq.pop()
                #print(arrseq)
                #print('3',s[i-2:i+1])
                #print('4',dct[s[i-2:i+1]])
                arrseq.append(dct[s[i-2:i+1]])
                #print(arrseq)
            else:
                #print('5',dct[s[i]])
                arrseq.append(dct[s[i]])
                #print(arrseq)
        for i in arrseq:
            res+=i
        return res

"""
First Commit: Solution completed. But, it can be groomed further.
"""