"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        clones = {}  # this is for the convernience of a deep copy
        clones[node] = Node(node.val) # you cant just do node = node, you have to create a new node object and replace its vals with the og one
        q = deque([node]) # q to do BFS, always uses the OG graph,
        while q:
            curr = q.popleft()  # always from the OG graph not from the clone, that way we can always access neighbors
            for neighbor in curr.neighbors: # we check each adjacent neighbor
                    if neighbor not in clones:
                        q.append(neighbor) # add to queue if it hasnt been visited yet to vsit later
                        clones[neighbor] = Node(neighbor.val)    # same concept of creating a new object
                    clones[curr].neighbors.append(clones[neighbor])# self explanatory, read it properly
                    
        return clones[node]


                
