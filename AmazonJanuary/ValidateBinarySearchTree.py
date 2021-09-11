# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_tree_valid(root,upper_bound,lower_bound):
            if root is None:
                return True
            
            if root.val <= lower_bound or root.val >= upper_bound:
                return False
            if root.left is not None:
                if root.val < root.left.val:
                    return False
            
            if root.right is not None:
                if root.val > root.right.val:
                    return False

            return is_tree_valid(root.left,root.val,lower_bound) and is_tree_valid(root.right,upper_bound,root.val) 

        return is_tree_valid(root,500000000000,-20000000000)