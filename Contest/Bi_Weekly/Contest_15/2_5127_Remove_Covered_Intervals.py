"""
Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

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
        dct={}
        if len(intervals)==1:
            return 1
        if len(intervals)==2:
            if intervals[0][0] <= intervals[1][0] and intervals[0][1] >= intervals[1][1]:
                return 1
            else:
                return 2
        removeCount=0
        for i in range(0,len(intervals)-removeCount-1):
            if intervals[i-removeCount][0]==intervals[i+1-removeCount][0]: #remove same start and keep lengthy one interval
                #print('First',intervals[i-removeCount])
                intervals.pop(i-removeCount)
                removeCount+=1
            elif intervals[i-removeCount][1]>=intervals[i+1-removeCount][1]:
                #print('Second',intervals[i+1-removeCount])
                intervals.pop(i+1-removeCount)
                removeCount+=1
        return len(intervals)

"""
Solved.But after contest was closed
"""