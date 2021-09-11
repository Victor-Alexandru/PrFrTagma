# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        current_pointer = ListNode()
        head = current_pointer
        transport = 0

        while  (l1 is not None) and (l2 is not None):
            aux = ListNode()
            current_pointer.val = (l1.val + l2.val  + transport ) % 10
            transport = ( l1.val + l2.val + transport ) // 10

        
            if l1.next is not None and l2.next is not None:
                current_pointer.next = aux
                current_pointer = aux
        
            l1 = l1.next
            l2 = l2.next
            
        if  l1 is None:
            while l2 is not None:
                aux = ListNode(val= (l2.val  + transport ) % 10)
                transport = (l2.val + transport) / 10 
                current_pointer.next = aux                
                current_pointer = aux
                l2 = l2.next

        if  l2 is None:
            while l1 is not None:
                aux = ListNode(val= (l1.val  + transport ) % 10)
                transport = (l1.val + transport) / 10 
                current_pointer.next = aux                
                current_pointer = aux
                l1 = l1.next

        if transport!=0:
            aux = ListNode(val=transport)
            current_pointer.next = aux



        return head

# 29 