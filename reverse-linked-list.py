# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        new_head = None
        next_node = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_node

        return new_head
