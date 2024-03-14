public class TreeNode {
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
public class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean isValidBST(TreeNode node, long min, long max) {
        if (node == null) {
            return true;
        }

        if (node.val <= min || node.val >= max) {
            return false;
        }

        return isValidBST(node.left, min, node.val) && isValidBST(node.right, node.val, max);
    }
}



// We define a TreeNode class representing the nodes of the binary tree.
// Create a Solution class containing a public method `isValidBST` that takes the root node of the binary tree as input and returns a boolean indicating the tree is a valid BST.
// At each node, it checks if the node's value is within the valid range defined by `min` and `max`. If the node's value violates this range, the method returns false, that the tree is not a valid BST.
// If the current node is null, the method returns true.
// Use `long` type for `min` and `max` parameters to handle edge cases where node values might be at the limits of integer range.
