# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkValidBST(root, -math.inf, math.inf)
        

    def checkValidBST(self, root, lower, upper):

        if root is None:
            return True

        return (
            (root.val > lower and root.val < upper) and \
            self.checkValidBST(root.left, lower, min(upper, root.val)) and \
            self.checkValidBST(root.right, max(lower, root.val), upper)
         )
