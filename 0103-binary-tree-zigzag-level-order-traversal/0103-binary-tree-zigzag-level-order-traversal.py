from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if not root: return []


        result = []
        queue = deque([root])

        lefttoRight = True
        
        while queue:

            size = len(queue)

            level = deque()

            for i in range(size):

                node = queue.popleft()

                if not lefttoRight:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            lefttoRight = not lefttoRight
            result.append(list(level))

        return result



