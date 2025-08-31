""" Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping. """



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0]) # this is to sort the array based on the first element of the sub array
        merged_array = [intervals[0]]
        for start, end in intervals[1:]: # checking the beginning adn ending element of each subarray excluding the first bc we alr initliazed it
            if merged_array[-1][1] >= start: # think of it as a number line we need to check if the latest merged array's end is greater than or equal to the beginning of the array thats supposed to come after it, if its larger then theres a conflict and we should merge these arrays
                merged_array[-1][1] = max(merged_array[-1][1], end) # here we use the max funciton cuz imagine if we had [1,6], [2,4] we would want to use 6 not 4 in this case
            else:
                merged_array.append([start,end]) # if theres no merge then lets start a new array to begin to check if theres a merge going on after it

        return merged_array
