# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rez = []

        children = []

        children.append(root)

        while(len(children)!=0):
            curr_level = []
            curr_level_values = []
            
            while len(children)!=0:
                item = children.pop(0)
                if item:
                    curr_level.append(item)
                    curr_level_values.append(item.val)

            for item in curr_level:
                if item.left:
                    children.append(item.left)
                if item.right:
                    children.append(item.right)
            if curr_level_values:
                rez.append(curr_level_values)
        
        return rez
