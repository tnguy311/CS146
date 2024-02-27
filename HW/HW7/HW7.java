class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // Sort intervals based on start time
        
        PriorityQueue<Integer> rooms = new PriorityQueue<>();
        rooms.add(intervals[0][1]); // Add end time of the first meeting

        for (int i = 1; i < intervals.length; i++) {
            if (rooms.peek() <= intervals[i][0]) {
                rooms.poll(); // Remove meeting ended
            }
            rooms.add(intervals[i][1]); // Add current meeting end time.
        }
        return rooms.size();
    }
}
