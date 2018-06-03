import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # ^       Start of line
        # [-+]?   Optional +-
        # [0-9]+  One or more [0-9]
        result = re.search("^[-+]?\d+", str.lstrip(" "))

        if result is not None:
            int_result = int(result.group())
            if int_result > 2147483647:
                return 2147483647
            elif int_result < -2147483648:
                return -2147483648
            else:
                return int_result
        return 0
