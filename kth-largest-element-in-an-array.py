class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # # Alternatively, we can use a heap
        # # Note: heapq uses min-heaps, so the runtime is actually
        # # O(n + (n-k)logn)
        # from heapq import heapify, heappop
        #
        # # O(n)
        # heapify(nums)
        # # O((n-k)logn)
        # for i in range(len(nums)+1-k):
        #     smallest = heappop(nums)
        #
        # return smallest

        # O(nlogn)
        nums = sorted(nums, reverse=True)
        return nums[k-1]
