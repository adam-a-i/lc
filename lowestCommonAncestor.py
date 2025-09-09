"""
235. Lowest Common Ancestor of a Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root.val > q.val and root.val < p.val) or (root.val < q.val and root.val > p.val): #this checks if its a break point for p,q meaning that they split fromhere in the BST bc one is bigger than the root and the other is smaller, if thats the case then the current root will be the last ancestor
            return root
        elif root.val == q.val: # if the root is one of p,q then its gonna be the latest ancestor
            return q
        elif root.val == p.val: # if the root is one of p,q then its gonna be the latest ancestor
            return p
        else:
            if p.val < root.val: # getting here means that p,q are 100% on the same sub tree of the root, so we just chceck one of the values and see if its less than or greater than the root and check the next subtree based off of that
                return self.lowestCommonAncestor(root.left, p,q) 
            else:
                return self.lowestCommonAncestor(root.right, p,q)

            
        
