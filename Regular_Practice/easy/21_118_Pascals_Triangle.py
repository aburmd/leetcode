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
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return None
        if numRows==1:
            self.dct[numRows]=[[1]]
            return self.dct[numRows]
        else:
            if numRows not in self.dct.keys():
                outerArray=[]
                for i in self.generate(numRows-1):
                    outerArray.append(i)
                innerArray=[]
                lastElement=outerArray[-1]
                for i in range(0,numRows):
                    if i==0 or i==(numRows-1):
                        innerArray.append(1)
                    else:
                        innerArray.append(lastElement[i-1]+lastElement[i])
                outerArray.append(innerArray)
                self.dct[numRows]=outerArray
                return self.dct[numRows]
            else:
                return self.dct[numRows]


"""
FirstCommit:
Runtime: 28 ms, faster than 83.98% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
"""


