class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.strings = list()
        self._generateParenthesis("(", n-1, n)

        return self.strings


    def _generateParenthesis(self, curr_str, num_open, num_close):
        """
        Recursively generate a valid parenthesis string
        based on a current string and the number of open and close brackets
        remaining to be appended
        """
        # Base case
        # Add last close bracket and add to strings
        if num_open == 0 and num_close == 1:
            self.strings.append(curr_str + ")")
            return

        # As long as the number of open brackets is <= the number of close brackets
        # We can append an open bracket
        if num_open > 0 and num_open <= num_close:
            self._generateParenthesis(curr_str + "(", num_open - 1, num_close)

        # As long as the number of close brackets is > the number of open brackets
        # We can append a close bracket
        if num_close > num_open:
            self._generateParenthesis(curr_str + ")", num_open, num_close - 1)
        
