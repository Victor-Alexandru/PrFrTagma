# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# public boolean isSymmetric(TreeNode root) {
#     return isMirror(root, root);
# }

# public boolean isMirror(TreeNode t1, TreeNode t2) {
#     if (t1 == null && t2 == null) return true;
#     if (t1 == null || t2 == null) return false;
#     return (t1.val == t2.val)
#         && isMirror(t1.right, t2.left)
#         && isMirror(t1.left, t2.right);
# }
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_Mirror(root,root_two):
            if root is None and root_two is None:
                return True
            if root is None or root_two is None:
                return False
            return root.val == root_two.val and is_Mirror(root.right,root_two.left) and  is_Mirror(root.left,root_two.right)


        return is_Mirror(root,root)
        
# Complexity Analysis

#Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total 
#run time is O(n)O(n), where nn is the total number of nodes in the tree.

#Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n)O(n).
#Therefore, space complexity due to recursive calls on the stack is O(n)O(n) in the worst case.

