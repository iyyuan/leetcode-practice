class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        # Create a mapping of digits to chars
        self.letters = dict()
        self.letters["2"] = ["a", "b", "c"]
        self.letters["3"] = ["d", "e", "f"]
        self.letters["4"] = ["g", "h", "i"]
        self.letters["5"] = ["j", "k", "l"]
        self.letters["6"] = ["m", "n", "o"]
        self.letters["7"] = ["p", "q", "r", "s"]
        self.letters["8"] = ["t", "u", "v"]
        self.letters["9"] = ["w", "x", "y", "z"]

        self.output = list()
        self._letterCombinations("", digits)
        return self.output

    def _letterCombinations(self, curr_str, digits):
        """
        Helper method to compute letter combinations of a digit
        """
        if len(digits) == 0:
            self.output.append(curr_str)
            return

        digit_chars = self.letters[digits[0]]
        for i, v in enumerate(digit_chars):
            self._letterCombinations(curr_str + v, digits[1:])
