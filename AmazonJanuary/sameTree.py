# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

#Complexity Analysis
# Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.

# Space complexity : O(log(N)) in the best case of completely balanced tree O(N)
#  in the worst case of completely unbalanced tree, to keep a recursion stack.

#[1,2,1]
#[1,1,2]

n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(1,n1,n2)


p1 = TreeNode(2)
p2 = TreeNode(1)
p3 = TreeNode(1,p2,p1)

s = Solution()   
print(s.isSameTree(None,None))



