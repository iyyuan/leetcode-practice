# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Need to store all nodes
        mem = list()

        current = head
        while current is not None:
            mem.append(current)
            current = current.next

        size = len(mem)

        # Attempting to remove past the head, so just
        # return head.next
        if n >= size:
            return head.next

        # Cannot do mem[size-n+1] because this might be None
        # and thus does not exist in our memory of all nodes
        mem[size-n-1].next = mem[size-n].next
        return head
