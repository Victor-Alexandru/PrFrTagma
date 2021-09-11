# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rez = []
        queue = [root]
        level = 1
        while len(queue)!=0:
            number_of_elements = len(queue)
            current_level = []
            for i in range(number_of_elements):
                current_level.append(queue.pop(0))
            
            if level % 2 == 0:
                for i in range(len(current_level)-1,-1,-1):
                    if current_level[i].left:
                        queue.append(current_level[i].left)
                    if current_level[i].right:
                        queue.append(current_level[i].right)
            else:
                for i in range(len(current_level)-1,-1,-1):
                    if current_level[i].left:
                        queue.append(current_level[i].right)
                    if current_level[i].right:
                        queue.append(current_level[i].left)
            
            level +=1
            current_level= [x.val for x in current_level]
            rez.append(current_level)
        
        return rez
# 35 