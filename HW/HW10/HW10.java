public class BinaryTreeTraversal {
   
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {}

        TreeNode(int val) { this.val = val; }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    
    static class Solution {
        public List<List<Integer>> levelOrder(TreeNode root) {
            List<List<Integer>> result = new ArrayList<>();
            if (root == null)
                return result;

            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);

            while (!queue.isEmpty()) {
                int size = queue.size();
                List<Integer> levelNodes = new ArrayList<>();
                for (int i = 0; i < size; i++) {
                    TreeNode current = queue.poll();
                    levelNodes.add(current.val);
                    if (current.left != null)
                        queue.add(current.left);
                    if (current.right != null)
                        queue.add(current.right);
                }
                result.add(levelNodes);
            }
            return result;
        }
    }

    
    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(3);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(1);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(9);

        Solution solution = new Solution();
        List<List<Integer>> traversalResult = solution.levelOrder(root);
        System.out.println(traversalResult);  
    }
}

// The TreeNode class defines a node in a binary tree.
// The Solution class implements the levelOrder method, which conducts a level-order traversal of a binary tree. 
//It uses a queue-based approach to traverse the tree level by level, storing the values of nodes at each level in a list of lists.
//  The main method acts as a testing environment for the BinaryTreeTraversal class. Creates a sample binary tree, calls the levelOrder method to perform the traversal and displays the resulting level-order traversal on the console.
