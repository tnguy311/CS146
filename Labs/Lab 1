import java.util.HashMap;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        // Create a special box called HashMap to remember things
        HashMap<Integer, Integer> complementMap = new HashMap<>();

        // Go through each number in the list
        for (int i = 0; i < nums.length; i++) {
            // Calculate a special number that, when added to the current number, gives the target
            int complement = target - nums[i];
            
            // Check if the special number is already in our special box
            if (complementMap.containsKey(complement)) {
                // If it's there, we found our two numbers! Return their positions
                return new int[]{complementMap.get(complement), i};
            }

            // If the special number is not in our box, put the current number in the box
            complementMap.put(nums[i], i);
        }

        // If we don't find the numbers, return an empty answer
        return new int[]{};
    }

    public static void main(String[] args) {
        // Some example numbers
        int[] nums = {2, 7, 11, 15};
        // Our target sum that we want to achieve
        int target = 9;
        // Use our function to find the two numbers
        int[] result = twoSum(nums, target);

        // Print the result (the positions of the two numbers)
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
