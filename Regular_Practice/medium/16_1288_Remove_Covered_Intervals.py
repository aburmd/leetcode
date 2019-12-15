"""Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.



Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.


Constraints:

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
intervals[i] != intervals[j] for all i != j
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last=0
        n=1 if len(intervals) else 0
        for i in range(1,len(intervals)):
            if intervals[i][0] == intervals[last][0]:
                last=i
            else:
                if intervals[i][1] > intervals[last][1]:
                    n+=1
                    last=i
        return n

"""
Second Commit: First will be available in Contest_15 tab 5127 problem
Runtime: 108 ms, faster than 100.00% of Python3 online submissions for Remove Covered Intervals.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Remove Covered Intervals."""

