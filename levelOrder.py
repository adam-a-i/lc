# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #BFS approach, anyhting to do w level order traversal its BFS
        res = []
        if not root:
            return []
        curr = root
        queue = deque([root]) # we always use a deque in BFS, the elements in the deque will always belong to the same level
        while queue:
            level = []
            for _ in range(len(queue)): # gothrough each root on the same level and pop them and add them to the level array, check if they have kids and if so add them, the next deque for the next iteration will be a level of roots 
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level) # add the current level

        return res


            
        
