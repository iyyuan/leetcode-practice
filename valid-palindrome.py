class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        # Technically can't use \W in the regex, since
        # \W = [^a-zA-Z0-9_]
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        # Could do pointers and check characters individually
        # But a palindrome is equal to itself reversed and we
        # can check that instead
        return s == s[::-1]
