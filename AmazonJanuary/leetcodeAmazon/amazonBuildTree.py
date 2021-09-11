# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        

        def counstruct_tree(root,inorder,postorder):
            if inorder == [] and postorder == []:
                return None
            last_elem = postorder[-1]
            root.val = last_elem
            left_inorder = []
            right_inorder = []
            for_left_inorder = True
            for i in range(len(inorder)):
                if inorder[i] == last_elem:
                    for_left_inorder = False
                elif for_left_inorder:
                    left_inorder.append(inorder[i])
                else:
                    right_inorder.append(inorder[i])
            left_postorder = []
            for i in range(len(left_inorder)):
                left_postorder.append(postorder[i])
            right_postorder = postorder[len(left_inorder):len(postorder)-1]
            left = TreeNode()
            right = TreeNode()
            root.left = counstruct_tree(left,left_inorder,left_postorder)
            root.right = counstruct_tree(right,right_inorder,right_postorder)
            return root

        a = TreeNode()
        if inorder == [] and postorder == []:
                return None
        counstruct_tree(a,inorder,postorder)
        return a

s = Solution()
print(s.buildTree(inorder = [9,3,15,20,7],postorder = [9,15,7,20,3]))