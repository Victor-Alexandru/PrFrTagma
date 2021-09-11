# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        current_node = head

        while current_node!= None:
            aux = current_node.next 
            current_node.next = prev_node
            prev_node = current_node
            current_node = aux

        return current_node

#7min