class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_counter = 0
        blue_counter = len(nums)-1

        # Move all 0's (reds) to the left
        # Move all 0's (blues) to the right
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > red_counter:
                # Only swap reds that have an index > the furthest red index from the start
                # Everytime we make a swap, we can't advance the index
                # since we might need to swap again
                self.swap(nums, i, red_counter)
                red_counter += 1
                i -= 1
            elif nums[i] == 2 and i < blue_counter:
                # Only swap reds that have an index < the furthest blue index from the end
                # Everytime we make a swap, we can't advance the index
                # since we might need to swap again
                self.swap(nums, i, blue_counter)
                blue_counter -= 1
                i -= 1
            i += 1

    def swap(self, nums, i1, i2):
        """
        Swap function
        """
        temp = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = temp
