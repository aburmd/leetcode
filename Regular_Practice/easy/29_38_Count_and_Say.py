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
    def __init__(self):
        self.saydct={}
    def countAndSay(self, n: int) -> str:
        if n==1:
            return str(1)
        else:
            if n in self.saydct.keys():
                return self.saydct[n]
            else:
                preval=self.countAndSay(n-1)
                count,next_say=1,[]
                for prev,curr in zip(preval[:-1],preval[1:]): #Great idea for comparing adjust values upto n-1 value
                    if prev==curr:
                        count+=1
                    else:
                        next_say.append(str(count)+prev)
                        count=1
                next_say.append(str(count)+preval[-1])
                self.saydct[n]=''.join(next_say)
            return self.saydct[n]

"""
SecondCommit: DP with recursive function. Much simple and powerful solution for this problem.
Runtime: 28 ms, faster than 91.63% of Python3 online submissions for Count and Say.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Count and Say.

FirstCommit: 
Runtime: 36 ms, faster than 36.28% of Python3 online submissions for Count and Say.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Count and Say.
"""