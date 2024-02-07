import java.util.Arrays;

public class Solution {
    public boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        char[] aArray = a.toCharArray();
        char[] bArray = b.toCharArray();
        Arrays.sort(aArray);
        Arrays.sort(bArray);
        return Arrays.equals(aArray, bArray);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String a = "silent";
        String b = "listen";
        boolean result = solution.isAnagram(a, b);
        System.out.println(result);
    }
}
