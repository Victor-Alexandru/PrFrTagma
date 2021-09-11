# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if  lists == []:
            return None
        
        root = None        
        head = None

        heads = PriorityQueue()
        #getting the heads
        for lk_list in lists:
            if lk_list is not None :
                heads.put(lk_list)

        if heads == []:
            return None

        while not heads.empty():
            if not root:
                root  = heads.get()
                head = root
                if root.next:
                    heads.put(root.next)
            else:
                root.next = heads.get()
                root = root.next
                if root.next:
                    heads.put(root.next)

        return head


s = Solution()
print(s.mergeKLists([[1,4,5],[1,3,4],[2,6]]))