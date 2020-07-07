# Definition for a binary tree node.
from typing import Iterable


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.paths = []
        self.search(root, ())
        return self.paths

    def search(self, root, paths):
        if not root.left and not root.right:
            self.paths.append("->".join(paths + tuple(str(root.val))))

        if root.left:
            self.search(root.left, paths + tuple(str(root.val)))
        if root.right:
            self.search(root.right, paths + tuple(str(root.val)))
