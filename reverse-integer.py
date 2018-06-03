class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            num = -int((str(x)[1:])[::-1])
        else:
            num = int(str(x)[::-1])

        # Hardcoded numbers for performance
        if (num < -2147483648) or (num > 2147483647):
            return 0
        else:
            return num
