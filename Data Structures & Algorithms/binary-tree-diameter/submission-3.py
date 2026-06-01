# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        # intuition:
        # diameter = distance of farthest node of left ST from root + distance of farthest node of right ST from root
        # depth + calculate max of nonlocal diameter (Global) and farthest left + farthest right
        def depth(node):
            nonlocal diameter

            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
            
            left = depth(node.left)
            right = depth(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        depth(root)

        return diameter