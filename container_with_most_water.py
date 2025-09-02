"""11. Container With Most Water
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 """



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
      """
      the logic behind this is to use the 2 pointer method bc brute forcing would be o(n^2), now we set the left pointer at the first index and the right at the last index
      we keep looping through the array till the right and the left index meet
      in the beginning of each loop we claculate the area by min(height[right], height[left]) * (right-left), we find the minumum height bc if oine rod is 8 and the other is 5 we can only go upto t 5 and not height and therefore we calculate the height with 5(min)
      if the right rod is larger than he left it oesnt mkae sense to move the right one inside bc if we do we'll either end up with a taller rod but it doesnt make a difference bc the left one is shroter anyway and at the same time we decrease the area by decreasing the width
      so we move the left pointer inwards in hopes of finding a taller rod to make the area bigger

      while looping through all this we keep track of the maximum area

      and ya thats it

      the else statement(where both heuights r equal) is random, it doesnt mkae a difference which one you move

      """
        left = 0
        right = len(height) - 1
        max_area = 0

        while right > left: # loops till both pointers meet
            if max_area < min(height[right], height[left]) * (right-left):
                max_area = min(height[right], height[left]) * (right-left)
            if height[right] > height[left]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
    
        return max_area


        
