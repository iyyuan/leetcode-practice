class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = list()
        nums.sort()

        for i, v in enumerate(nums):

            # To pass the test of a list of many zeros...
            if i >= 1 and v == nums[i-1]:
                continue

            # The two-sum value we are trying to find
            value = -v

            mem = {}
            # Only need to check the rest of the array going forward
            for x in nums[i+1:]:
                if value-x in mem:
                    sol.append(sorted([-value, value-x, x]))
                else:
                    mem[x] = 1

        return([list(x) for x in set(tuple(x) for x in sol)])
