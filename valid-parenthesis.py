class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        stack = list()

        for c in list(s):
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            if c == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif c == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif c == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False

        # The stack must be empty for a set of valid parenthesis
        # E.g. input of "[" should return False
        if len(stack) > 0:
            return False
        return True
