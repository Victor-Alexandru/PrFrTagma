# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heads_lists = []

        heapq.heapify(heads_lists)
        for head in lists:
            if head:
                heapq.heappush(heads_lists,(head.val,head))

        if heads_lists  == []:
            return None
        
        val,current_element = heapq.heappop(heads_lists)

        return_head = current_element
        current_pointer = current_element

        if current_element.next:
            heapq.heappush(heads_lists,(current_element.next.val,current_element.next))
        
        while  heads_lists != []:
            val,current_element = heapq.heappop(heads_lists)
            if current_element.next:
                    heapq.heappush(heads_lists,(current_element.next.val,current_element.next))
            current_pointer.next = current_element
            current_pointer = current_element

        return return_head
            
        
