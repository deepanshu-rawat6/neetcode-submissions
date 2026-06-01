# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # BFS + 2 queue pattern, 
        queue_p, queue_q = deque([p]), deque([q])
        while queue_p and queue_q:
            for _ in range(len(queue_p)):
                node_p = queue_p.popleft()
                node_q = queue_q.popleft()

                # was stuck here, as in first test case: [1,2,3] and [1,2,3], we can skip null nodes by this check otherwise
                # it casused issues with node_p or node_q getting null in case of leaf nodes.
                if not node_p and not node_q:
                    continue

                if not node_p or not node_q or node_p.val != node_q.val:
                    return False
                
                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)
        
        if queue_p or queue_q:
            return False
        else:
            return True
        