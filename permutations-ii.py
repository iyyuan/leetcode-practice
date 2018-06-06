class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = list()
        self._permuteUnique(list(), nums)
        return self.output


    def _permuteUnique(self, curr_arr, nums):
        """
        Helper method to compute permutations recursively using a
        local dict() to deal with duplicates
        """
        mem = dict()

        if not nums:
            self.output.append(curr_arr)
            return

        for i, v in enumerate(nums):
            if v in mem:
                continue
            else:
                mem[v] = 1
                new_arr = list(curr_arr)
                new_arr.append(v)
                self._permuteUnique(new_arr, nums[:i] + nums[i+1:])
