class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Easy solution of O(xlogx) where x = m+n
        nums = sorted(nums1 + nums2)
        n = len(nums)
        # Floor division result
        m = n // 2

        if n % 2 == 1:
            return nums[m] / 1.0
        else:
            return (nums[m] + nums[m-1]) / 2.0
