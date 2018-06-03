class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = dict()
        n["M"] = 1000
        n["D"] = 500
        n["C"] = 100
        n["L"] = 50
        n["X"] = 10
        n["V"] = 5
        n["I"] = 1

        num = 0
        i = 0

        while i < len(s)-1:
            # One character for 1 value
            if n[s[i]] >= n[s[i+1]]:
                num += n[s[i]]
                i += 1
            else:
                # Need to combine two characters for 1 value
                # e.g. IV = 4, IX = 9, etc.
                num += (n[s[i+1]] - n[s[i]])
                i += 2

        # Add the last character if we haven't already
        if i == len(s)-1:
            num += n[s[-1]]

        return num
