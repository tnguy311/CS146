public class Solution {
    public int badVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}


/*Using binary search algorithm and find the first bad version.
Initialize two pointers, left and right, representing the range of versions to search within.
While left < right, calculate the midpoint.
Then check if mid is a bad version using the isBadVersion API:
If mid is a bad version, right = mid to search in the left half.
If mid is not a bad version, left = mid + 1 to search in the right half.
Repeat the process until left and right converge; left == right.
Return left, which represents the first bad version.*/
