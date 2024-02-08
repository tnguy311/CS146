import java.util.HashMap;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int target = 17;
        int[] result = twoSum(nums, target);
        System.out.println(result[0] + " " + result[1]);
    }

/*Initialize a HashMap to store the numbers seen so far, with the key being the number and the value being its index in the array.
Iterate through the array 'nums'.
Calculate the complement by subtracting the current number from the target.
Check if the complement exists in the HashMap:
If the complement exists, return the indices of the current number and its complement.
If the complement doesn't exist, store the current number and its index in the HashMap.
If the loop completes without finding a solution, use an IllegalArgumentException.
In the main method, create an array of numbers 'nums' and specify the target sum.
Call the 'twoSum' method and print the indices of the two numbers that add up to the target.*/
