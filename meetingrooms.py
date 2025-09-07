"""
Meeting Rooms II
Solved 
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = [] # keeps track of minmum end time, smallet end time is always at index 0

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start: # if the current intervals start time is greater than the meeting thats abt to end end time that means there wont be a conflict so we piop that one out adnintorudce our new meeting, otherwise dont pop it out bc both will be happening at once
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

# Min-heap stores end times of ongoing meetings.
# Heap[0] = earliest ending meeting (the room that frees first).
# For each meeting:
#   - If start >= heap[0], reuse that room (pop & push new end).
#   - Else, conflict → need new room (push new end).
# Heap size at any moment = number of rooms in use.
# Max heap size reached = minimum rooms required.



