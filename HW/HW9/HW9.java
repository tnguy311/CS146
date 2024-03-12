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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode currentNode = root;
        
        while (currentNode != null) {
            if (p.val < currentNode.val && q.val < currentNode.val) {
                currentNode = currentNode.left;
            } else if (p.val > currentNode.val && q.val > currentNode.val) {
                currentNode = currentNode.right;
            } else {
                return currentNode;
            }
        }
        
        return null;
    }
}


// Start from the root node of the tree
// Loop until we find the LCA
// Then if both nodes p and q are smaller than currentNode, move to the left child
// If both nodes p and q are larger than currentNode, move to the right child
// If the above conditions are false, it means we have found the split point,
// either both p and q are on different sides of currentNode, or one of p or q is equal to currentNode.
// return null indicating the LCA wasn't found.
