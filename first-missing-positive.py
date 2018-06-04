class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TODO: Challenge is to find a solution with O(1)
        # space complexity and O(N) time complexity
        # The following solution is O(N) for time and space

        # Space complexity O(N)
        m = dict()

        # Time complexity O(N)
        for num in nums:
            m[num] = 1

        index = 1
        # Time complexity O(N)
        while index in m:
            index += 1

        return index
