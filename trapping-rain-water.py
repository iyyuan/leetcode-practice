class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0

        max_left = [0] * n
        max_right = [0] * n

        # Compute the maximum height to the left of each tower
        max_left[0] = height[0]
        for i in range(n):
            max_left[i] = max(height[i], max_left[i-1])

        # Compute the maximum height to the right of each tower
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])

        # The amount of water for each index is the minimum of
        # the max_left[i] and max_right[i] minus the height of the tower
        # at index i
        total = 0
        for i in range(n):
            total += min(max_left[i], max_right[i]) - height[i]

        return total
