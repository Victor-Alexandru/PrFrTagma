#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return

        #O(n)
        def find_tail_and_lenght(node,counter=1):
            if node.next is None:
                return [node,counter]
            else:
                counter+=1
                return find_tail_and_lenght(node.next,counter)

        #O(n) 
        def find_new_tail(root,index_stop,counter):
            if counter == index_stop:
                return root
            else:
                counter += 1
                return find_new_tail(root.next,index_stop,counter)   

        tail = find_tail_and_lenght(head)[0]
        n = find_tail_and_lenght(head)[1]
        tail.next = head
        head_counter = n - (k%n) 
        new_tail = find_new_tail(head,head_counter,counter=1)
        head = new_tail.next
        new_tail.next = None

        return head

a = ListNode(2,None)
b = ListNode(1,a)
c = ListNode(0,b)

s  = Solution()
print(s.rotateRight(c,4))