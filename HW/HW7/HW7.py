class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
        rooms = []  # Heap to store end times of meetings
      
      for start, end in intervals:
            if rooms and rooms[0] <= start:
                heappop(rooms)  # Remove meeting that ended
            heappush(rooms, end)  # Add current meeting end time

        return len(rooms)
