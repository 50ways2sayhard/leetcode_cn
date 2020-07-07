# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        return self.bound(root, -(2 ** 32), 2 ** 32)

    def bound(self, root: TreeNode, lower: int, upper: int) -> bool:
        if not root:
            return True

        middle = lower < root.val < upper
        if not middle:
            return False
        return self.bound(root.left, lower, root.val) and self.bound(
            root.right, root.val, upper
        )
