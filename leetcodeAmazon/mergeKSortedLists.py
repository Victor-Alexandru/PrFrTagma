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

        if lists == []:
            return []

        heads_list = []

        for linked_list in lists:
            if linked_list is not None:
                heads_list.append((linked_list.val,linked_list))
        
        if heads_list == []:
            return []

        heapq.heapify(heads_list)

        head = heapq.heappop(heads_list)[1]
        if head.next:
            heapq.heappush(heads_list,(head.next.val,head.next))

        current_pointer = head
        
        while len(heads_list) != 0 :

            min_element = heapq.heappop(heads_list)[1]

            if min_element.next:
                heapq.heappush(heads_list,(min_element.next.val,min_element.next))

            current_pointer.next = min_element
            current_pointer = min_element


        return head


        