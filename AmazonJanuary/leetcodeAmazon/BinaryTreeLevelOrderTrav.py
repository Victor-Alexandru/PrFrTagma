class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rez = []
        def level_traversal(root,level=1):
            if root is not None:
                if len(rez) < level:
                    rez.append([])
                    rez[level-1].append(root.val)
                else:
                    rez[level-1].append(root.val)

                level = level+1 
                level_traversal(root.left,level)
                level_traversal(root.right,level)

        level_traversal(root)


        return rez

#13