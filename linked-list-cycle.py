# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Could hash all pointers in a dict - O(n) space
        # Or just use two pointers - O(1) space
        # aka Floyd's cycle finding algorithm
        ptr1 = head
        ptr2 = head

        while ptr1 and ptr2 and ptr2.next:
            # Advance one pointer by 1 node
            # and the other by 2 nodes
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

            # If they are the same ptr, there is a cycle
            if ptr1 == ptr2:
                return True

        return False
