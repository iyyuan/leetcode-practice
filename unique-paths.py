class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = list()

        # Initialize the 2D grid
        for i in range(n):
            temp = [0] * m
            grid.append(temp)

        # Topmost row are all 1's
        for i in range(m):
            grid[0][i] = 1

        # Leftmost column are all 1's
        for i in range(n):
            grid[i][0] = 1

        # All other spaces have a unique number of paths equal to
        # the sum of the space above and to the left of it
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i][j-1] + grid[i-1][j]

        return grid[n-1][m-1]
