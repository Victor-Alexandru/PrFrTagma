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
        
        queue = []
        levels = []

        if not root:
            return levels

        queue.append(root)

        while len(queue) != 0 :
            current_level = []
            current_queue_length = len(queue)
            
            for i in range(current_queue_length):
                elem = queue.pop(0)
                current_level.append(elem)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)

            levels.append(current_level)

        return levels            

