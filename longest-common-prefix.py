class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Empty list, return ""
        if len(strs) == 0:
            return ""

        # Single entry in list, return entry
        if len(strs) == 1:
            return strs[0]

        # Need to find the shortest length string
        shortest = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < shortest:
                shortest = len(strs[i])

        longest_prefix = ""
        index = 1

        # Iterate until index <= shortest, since
        # index will start at 1 to grab the first letter
        while index <= shortest:
            # Get the current prefix
            # Index starts at 1 since [0:0] is ""
            prefix = strs[0][0:index]

            # Return the longest_prefix if any of the strings
            # in the list do not start with the currently
            # evaluated prefix
            for i in range(1, len(strs)):
                if not strs[i].startswith(prefix):
                    return longest_prefix

            longest_prefix = prefix
            index += 1

        return longest_prefix
