"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def __init__(self):
        self.dct={}
    def lastElement(self, numRows):
        if numRows in self.dct.keys():
            return self.dct[numRows]
        else:
            if numRows==1:
                self.dct[numRows]=[1]
            elif numRows==2:
                self.dct[numRows]=[1,1]
            else:
                last=self.lastElement(numRows-1)
                x=[]
                for i in range(0,numRows):
                    if i==0 or i==numRows-1:
                        x.append(1)
                    else:
                        x.append(last[i-1]+last[i])
                self.dct[numRows]=x
            return self.dct[numRows]
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return None
        else:
            outerArray=[]
            for i in range(1,numRows+1):
                outerArray.append(self.lastElement(i))
            return outerArray


"""
SecondCommit:
Runtime: 24 ms, faster than 94.10% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
FirstCommit:
Runtime: 28 ms, faster than 83.98% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
"""


