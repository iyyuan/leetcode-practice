class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        ptr = 0
        longest = 0

        for i in range(len(s)):
            if s[i] in mem:
                longest = max([i-ptr, longest, 1])
                ptr = mem[s[i]]+1
                mem[s[i]] = i

                # Not very efficient, but it works
                new_mem = {}
                for j in mem.keys():
                    if mem[j] >= ptr:
                        new_mem[j] = mem[j]
                mem = new_mem
            else:
                mem[s[i]] = i

        longest = max([longest, len(s)-ptr])

        return longest
