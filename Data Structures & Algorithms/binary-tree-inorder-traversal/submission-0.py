# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversalInOrder(root):
            if root == None:
                return None
            
            traversalInOrder(root.left)
            ans.append(root.val)
            traversalInOrder(root.right)
            
        ans = []
        traversalInOrder(root)
        return ans
        