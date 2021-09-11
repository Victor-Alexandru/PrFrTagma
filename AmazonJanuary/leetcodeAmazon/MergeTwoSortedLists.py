# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        current_node = head
        
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2
        
        if l2 is None:
            return l1 

        while l1 is not None and l2 is not None:
            if l1.val  >= l2.val:
                if current_node is not None:
                    current_node.next = l2
                if not head:
                    head = l2

                current_node = l2
                l2 = l2.next
            else:  
                if current_node is not None:
                    current_node.next = l1
                
                if not head:
                    head = l1
                
                current_node = l1
                
                l1 = l1.next

        if l1 is None:
            while l2 is not None:
                current_node.next = l2
                current_node = l2
                l2 = l2.next

        if l2 is None:
            while l1 is not None:
                current_node.next = l1
                current_node = l1
                l1 = l1.next




        return head
#12:20
