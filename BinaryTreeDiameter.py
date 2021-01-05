# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        maxi = 0
        last_node = None
        if root is None:
            return maxi

        def traverse_tree(root,level=0):
            nonlocal maxi
            nonlocal last_node
            if root is not None:
                if level > maxi:
                    maxi = level
                    last_node = root

            if root.left:
                level +=1
                traverse_tree(root.left,level)
            if root.right:
                level +=1
                traverse_tree(root.left,level)

        traverse_tree(root)
        traverse_tree(last_node)

        return maxi
        