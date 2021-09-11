class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_mirror(root_one,root_two):
            if root_one is None and root_two is None:
                return True

            if root_one is not None and root_two is None:
                return False
            
            if root_two is not None and root_one is None:
                return False

            if root_one.val != root_two.val:
                return False
            
            return is_mirror(root_one.left,root_two.right) and is_mirror(root_one.right,root_two.left)

        return is_mirror(root,root)
      
#12 min O(n) space O(n)