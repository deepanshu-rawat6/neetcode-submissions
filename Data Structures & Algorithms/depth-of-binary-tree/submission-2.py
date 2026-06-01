# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # standard BFS + dequeu
        if not root:
            return 0
        
        ans, queue = 0, deque([root])

        while queue:
            ans += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return ans
        