from heapq import heappush, heappushpop
# from bisect import insort

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Need two heaps, one for the upper half of all the numbers
        # and another for the lower half of all the numbers
        # Then the median will be the minimum of the upper half of all numbers
        # and the maximum of the lower half of all numbers
        self.upper = []
        self.lower = []

        # # Using insort
        # self.data = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # heapq uses min-heaps
        # By negating the lower half of numbers and storing them in a min-heap, the
        # minimum of all these negative values can be made into the maximum of all the
        # lower half of numbers by negating it once more
        # heappushpop is equivalent to pushing num onto the heap, and popping the min
        num = heappushpop(self.upper, num)
        num = -heappushpop(self.lower, -num)

        if len(self.upper) <= len(self.lower):
            # Push the max of all lower half values onto the upper half
            heappush(self.upper, num)
        else:
            # Push the min of all upper half values onto the lower half
            heappush(self.lower, -num)

        # # Using insort
        # insort(self.data, num)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.upper) > len(self.lower):
            return self.upper[0] / 1.0
        else:
            return (self.upper[0] - self.lower[0]) / 2.0

        # # Using insort
        # n = len(self.data)
        # if n % 2 == 1:
        #     return self.data[n // 2] / 1.0
        # else:
        #     return (self.data[n // 2] + self.data[(n // 2) - 1]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
