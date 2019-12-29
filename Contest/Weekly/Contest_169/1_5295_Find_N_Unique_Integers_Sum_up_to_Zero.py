"""
Given an integer n, return any array containing n unique integers such that they add up to 0.



Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]


Constraints:

1 <= n <= 1000
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        else:
            x=[]
            inc=1
            for i in range(1,n+1):
                if i<=(n//2):
                    x.append(inc)
                    inc+=1
                else:
                    inc-=1
                    x.append(-1*inc)
            if n%2!=0:
                x[-1]=0
            return x


"""
First Commit:
Contest: Completed within that timeframe

"""