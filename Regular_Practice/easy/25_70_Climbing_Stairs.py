"""

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

class Solution:
    def __init__(self):
        self.dct={}
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            if n not in self.dct.keys():
                self.dct[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.dct[n]


"""
First Commit:
Runtime: 16 ms, faster than 99.58% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
"""

"""
Algorithm
As we can see this problem can be broken into subproblems, and it contains the optimal substructure property i.e. its optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic programming to solve this problem.

One can reach i(th) step in one of the two ways:

1) Taking a single step from (i-1)(th) step.
2) Taking a single step from (i-2)(th) step.

So, the total number of ways to reach i(th) is equal to sum of ways of reaching (i-1)(th) step and ways of reaching (i-2)(th) step.

let dp[i] denotes the number of ways to reach on i(th) step:
dp[i]=dp[i-1]+dp[i-2]
 
"""