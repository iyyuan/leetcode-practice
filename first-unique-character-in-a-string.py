class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = dict()

        for i, v in enumerate(s):
            if v in chars:
                chars[v] += 1
            else:
                chars[v] = 1

        for i, v in enumerate(s):
            if chars[v] == 1:
                return i

        return -1
