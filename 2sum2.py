"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2]
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointer problem
        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers)): # loop through whole array if needed
            if numbers[left] + numbers[right] > target: #since we know the target adn we know that the array is sorted if the sum of two numbers is larger than the target then we should move the right pointer to the left because we'd get a smaller number that could be our target
                right -= 1
            elif numbers[left] + numbers[right] == target:# if we find the target then return 
                return [left + 1, right + 1]
                break
            else: # if its smaller than the target than move the left pointer up cuz we know that even with the alrget number we cant get it to be big enough to get to the target, so we move upo to a bigger number adn check if itll work 
                left += 1


        
