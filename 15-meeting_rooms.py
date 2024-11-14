import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Initialize a min-heap to keep track of end times
        freeRoom = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            # If the room due to free up the earliest is free, remove it
            if freeRoom[0] <= intervals[i][0]:
                heapq.heappop(freeRoom)

            # Add the current meeting end time to the heap
            heapq.heappush(freeRoom, intervals[i][1])

        # The size of the heap tells us the minimum rooms required
        return len(freeRoom)

# Time Complexity = O(nlogn)
# Space Complexity = O(n)