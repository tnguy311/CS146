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

/*Sorting the characters in both strings and comparing if the sorted versions are equal.
In Java implementations, we use the Arrays.sort() method.
We then compare the sorted strings using the Arrays.equals() method.
If the lengths of the strings are different, they cannot be anagrams, so we return false.
Otherwise, we return the result of the comparison. If the sorted strings are equal, it means the strings are anagrams, so we return true otherwise, we return false.*/
