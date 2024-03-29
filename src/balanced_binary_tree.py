# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def get_height(root: TreeNode | None) -> int:
            if root is None:
                return 0
            return 1 + max(get_height(root.left), get_height(root.right))

        if root is None:
            return True
        else:
            return (
                abs(get_height(root.left) - get_height(root.right)) <= 1
                and self.isBalanced(root.right)
                and self.isBalanced(root.left)
            )
