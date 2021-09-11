"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue = []
        if not root:
            return None

        queue.append(root)
        
        while queue:
            current_queue_length = len(queue)
            
            for i in range(current_queue_length):
                if i+1 < current_queue_length-1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i+1]
            
            for i in range(current_queue_length):
                if queue[i].left:
                    queue[i].append(queue[i].left)
                if queue[i].right:
                    queue[i].append(queue[i].right)
                queue.pop(0)
            

        return root
    