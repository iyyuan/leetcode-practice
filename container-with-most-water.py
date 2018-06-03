class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        area = 0

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))

            # If a better solution exists, it has a min height > min(height[left], height[right])
            # Thus, if height[left] < height[right], the problem is to solve height[left+1], height[right]
            # Else, if height[right] > height[left], the problem is to solve height[left], height[right-1]
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area