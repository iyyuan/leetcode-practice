class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}

        for i in range(len(nums)):
            if (target-nums[i]) in mem:
                # Guarenteed to be at least 1 solution
                return [mem[target-nums[i]], i]
            else:
                mem[nums[i]] = i
