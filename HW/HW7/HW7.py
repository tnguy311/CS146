class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
        rooms = []  # Heap to store end times of ongoing meetings
      
      for start, end in intervals:
            if rooms and rooms[0] <= start:
                heappop(rooms)  # Remove the meeting that has ended
            heappush(rooms, end)  # Add the end time of the current meeting

        return len(rooms)
