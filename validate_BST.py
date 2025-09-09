# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def helper(node, left, right): # tests the bounds 

            if not node:
                return True
            if not ((node.val > left) and (node.val < right)):
                return False
            
            return helper(node.left, left, node.val) and helper(node.right, node.val, right) # this is a DFS apporach that makes sure that youre always checking if the left binary tree is allllll less than the root and vice versa for the right side

        return helper(root, float("-inf"), float("inf")) 
        
