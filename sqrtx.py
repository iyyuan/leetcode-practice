class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Haha, this would be so great
        # import math
        # return math.floor(math.sqrt(x))

        if x == 0 or x == 1:
            return x

        left = 1
        right = x

        while (left <= right) :
            mid = (left + right) // 2

            # Perfect square
            if mid * mid == x:
                return mid

            if mid * mid < x:
                # Too small, grow left value in BST
                left = mid + 1
                ans = mid
            else:
                # Too large, shrink right value in BST
                right = mid - 1

        return ans
