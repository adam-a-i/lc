class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0 # edge case
        droplets = 0 #increment result
        l, r = 0, len(height) -1
        maxL, maxR = height[l],height[r]
        
        while l < r: # initilaize two pointer
          if maxL < maxR: # this means that we should left inside to possibly find a height that can match the height of the maximum right boundary
                l+=1
                maxL = max(height[l], maxL) 
                droplets += maxL - height[l] # this follows the principle of the way of fidning droplets = min(maxL,maxR) - height[i]
            else:
                r-=1
                maxR = max(height[r], maxR)
                droplets += maxR - height[r]
           
        return droplets
        
             
