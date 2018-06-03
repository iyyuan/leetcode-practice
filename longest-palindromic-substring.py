class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        self.longest = ""

        for i in range(len(s)):
            # Find odd length palindromes
            self.findPalindrome(s, i, i)
            # Find even length palindromes
            self.findPalindrome(s, i, i+1)

        return self.longest

    def findPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Need to account for zero-based indexing
        if right - left - 1 > len(self.longest):
            self.longest = s[left+1:right]
