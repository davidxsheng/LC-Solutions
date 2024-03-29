# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def get_ancestors(child: TreeNode, root: TreeNode) -> list[int]:
            ancestors = []
            while True:
                ancestors.append(root.val)
                if root.val > child.val:
                    root = root.left
                elif root.val < child.val:
                    root = root.right
                else:
                    break
            return ancestors
        p_ancestors = get_ancestors(p, root)
        q_ancestors = get_ancestors(q, root)
        for ancestor_value in reversed(p_ancestors):
            if ancestor_value in q_ancestors:
                ancestor_to_return = ancestor_value
                break
        
        while True:
            if root.val > ancestor_to_return:
                root = root.left
            elif root.val < ancestor_to_return:
                root = root.right
            else:
                return root
        
        