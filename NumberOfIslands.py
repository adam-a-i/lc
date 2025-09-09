class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: #grids emppty
            return 0
        
        def bfs(r,c):
            q = deque() # always use queue from bfs
            visit.add((r,c))
            q.append([r,c])
            while q: # while the q isnt empty(meaning that there are still islands within the island that we havent visited)
                row,col = q.popleft()
                directions = [[0,1], [1,0], [-1,0], [0,-1]] # this lets us check bottom, up, left and right

                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r,c) not in visit): # if the adjacent 1 to the initia one from q is in the range of our grid, is actualy a 1, and we havent visited it yet, then add it to the queue to check its neighbors too and add it to visited
                        q.append([r,c])
                        visit.add((r,c))

        rows, col = len(grid), len(grid[0])
        visit = set() # to keep track of the 1's weve visited
        islands = 0

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit: # if the string is 1 and we havent already visited it then lets do bfs and check how far it extends on this position
                    bfs(r,c)
                    islands+=1 # since we found a new 1


        return islands





        
