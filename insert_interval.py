"""
Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



"""



class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        newarr = [] 
        merging = newInterval # this array will be used to keep track of all of the merging arrays to contenate them into one and append to our new array(newarr)
      """ the logic behind this solution has several steps: 
      1. append all non conflicting arrays to our new array before the merging conflict(to the left of the new interval), done by end < merging[0]
      2. once we apppend all the arays before the merge we get to the conflict the conflict does the following: merging = [min(merging[0], start), max(merging[1], end)] (similar to merge intervals problem)
      3. once we are done then this if statement will be satisfied: elif start > merging[1]:
                newarr.append(merging)
                newarr.append([start,end])
        this appends the conflict merging array and now we are done with the merging all thats left is to add all the arrays after the merge
        we set merging to None so that the first if statement repeatedly adds the rest of the non conflicting arrays after

        the reason we have the final if staatement before return is for edge cases like the array being empty, if its empty it wont go through the for loop and just directly append the new interval
      """
        for start, end in intervals:
            if not merging:
                newarr.append([start,end])
            elif end < merging[0]: 
                newarr.append([start,end])
            elif start > merging[1]:
                newarr.append(merging)
                newarr.append([start,end])
                merging = None
            else:
                 merging = [min(merging[0], start), max(merging[1], end)]
        if merging:
            newarr.append(merging)

        return newarr
