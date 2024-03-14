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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        if (root.left != null) {
            invertTree(root.left);
        }

        if (root.right != null) {
            invertTree(root.right);
        }

        return root;
    }
}

// If the tree is empty, we return null immediately as there's no need to invert an empty tree.
// For each non-null node in the tree, we swap its left and right children. 
// After swapping the children, we recursively call the `invertTree` function for both the left and right children of current node. This repeats the swapping process for each subtree.
// Then we return the root node of the inverted tree.
