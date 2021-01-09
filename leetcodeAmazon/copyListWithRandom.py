"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_head  = copy.deepcopy(head)

        if not new_head:
            return new_head

        cuurent_pointer = new_head
        head = head.next
        
        while head!=None:
            cuurent_pointer = copy.deepcopy(head)
            cuurent_pointer.next = cuurent_pointer
            head = head.next

        return new_head

        
        