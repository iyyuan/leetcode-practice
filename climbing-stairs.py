class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Create some form of memoization
        self.mem = dict()
        # Base cases
        self.mem[0] = 1
        self.mem[1] = 1
        self.mem[2] = 2
        return self._climbStairs(n-1) + self._climbStairs(n-2)

    def _climbStairs(self, n):
        if n < 0:
            return 0

        if n in self.mem:
            return self.mem[n]

        num_ways = self._climbStairs(n-1) + self._climbStairs(n-2)
        self.mem[n] = num_ways
        return num_ways
