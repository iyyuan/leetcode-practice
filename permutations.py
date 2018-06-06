class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = list()
        for i, v in enumerate(nums):
            self._permute([v], nums[:i] + nums[i+1:])
        return self.output


    def _permute(self, curr_arr, nums):
        """
        Helper method to compute permutations recursively
        """
        # Runs faster than len(nums) == 0
        if not nums:
            self.output.append(curr_arr)
            return

        for i, v in enumerate(nums):
            new_arr = list(curr_arr)
            new_arr.append(v)
            self._permute(new_arr, nums[:i] + nums[i+1:])
