# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count = 0
        currA = headA
        currB = headB

        # Figure out the difference in length for both lists
        while currA is not None:
            currA = currA.next
            count += 1

        while currB is not None:
            currB = currB.next
            count -= 1

        # Align both linked lists such that they start
        # from the same distance from the last node
        currA = headA
        currB = headB
        if count > 0:
            while count > 0:
                currA = currA.next
                count -= 1
        else:
            while count < 0:
                currB = currB.next
                count += 1

        # If we did this right, there is no need to check
        # the condition: (currB is not None)
        # since currB will be None when currA is None
        while currA is not None:
            if currA.val == currB.val:
                return currA
            currA = currA.next
            currB = currB.next

        return None
