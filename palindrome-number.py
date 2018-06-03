class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        s = str(x)

        # A palindrome is the same as itself reversed
        if s == s[::-1]:
            return True
        return False
