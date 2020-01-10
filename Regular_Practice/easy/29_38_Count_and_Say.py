"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return str(1)
        elif n==2:
            return str(11)
        else:
            x=self.countAndSay(n-1)
            count=0
            y=0
            res=''
            say=None
            for i in range(1,len(str(x))):
                if str(x)[y]==str(x)[i]:
                    #print('check1')
                    count+=1
                    say=str(x)[i]
                    y=i
                elif say:
                    #print('check2')
                    count+=1
                    res=res+str(count)
                    res=res+say
                    say=None
                    count=0
                    y=i
                else:
                    #print('check3')
                    count+=1
                    res=res+str(count)
                    res=res+str(x)[y]
                    y=i
                    count=0
            #print('check4')
            count+=1
            say=str(x)[len(str(x))-1]
            res=res+str(count)
            res=res+say
            return res

"""
FirstCommit: 
Runtime: 36 ms, faster than 36.28% of Python3 online submissions for Count and Say.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Count and Say.
"""