# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(root):
            if root is None:
                return root
            
            temp = root.right
            root.right = recurse(root.left)
            root.left = recurse(temp)

            return root

        return recurse(root)
