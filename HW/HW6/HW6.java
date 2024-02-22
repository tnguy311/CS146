    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);  // Sort the array 
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;    // skip duplicate fixed numbers
            
            int target = -nums[i];
            Set<Integer> seen = new HashSet<>(); 
            
            for (int j = i + 1; j < nums.length; j++) {
                int complement = target - nums[j];
                
                // if complemn is in the set, add the triplet to the result.
                if (seen.contains(complement)) {
                    result.add(Arrays.asList(nums[i], complement, nums[j]));
                    
                    // Skip duplicate numbers
                    while (j + 1 < nums.length && nums[j] == nums[j + 1])
                        j++;
                }
                
                seen.add(nums[j]);
            }
        }
        
        return result;
    }

    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {0, 1, 1};
        int[] nums2 = {-5, 0, 5, 10, -10, 0};
        System.out.println(solution.threeSum(nums1));
        System.out.println(solution.threeSum(nums2));
    }
}
