class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        mem = [0] * (len(s)+1)
        mem[len(s)] = 1
        mem[len(s)-1] = 1 if s[len(s)-1] != '0' else 0

        for i in range(len(s)-2, -1, -1):
            if s[i] > '0':
                mem[i] = mem[i+1] + mem[i+2] if int(s[i:i+2]) <= 26 else mem[i+1]

        return mem[0]
