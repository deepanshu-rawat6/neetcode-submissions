# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        isRev = True

        if not root:
            return []

        # Standard BFS + Queue pattern   
        res, queue = [], deque([root])
        while queue:
            # using deque for easier handling of left to right or right to left node
            level = deque()

            for _ in range(len(queue)):
                node = queue.popleft()

                if isRev:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            isRev = not isRev
            res.append(list(level))
        
        return res
        