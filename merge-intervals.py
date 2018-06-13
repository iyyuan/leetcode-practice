# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda x : x.start)

        stack = list()
        stack.append(intervals[0])

        for i in range(1, len(intervals)):

            prev = stack[-1]
            curr = intervals[i]
            if curr.start >= prev.start and curr.start <= prev.end:
                prev.end = max(prev.end, curr.end)
            else:
                stack.append(curr)

        return stack
