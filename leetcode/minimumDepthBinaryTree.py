# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root, queue=[]):
        # Concept: we're going to breadth-first search this
        # ISSUE: we totally could, but the problem is that we have difficulty keeping track of the depth. How can we fix that? We just store it
        if root == None:
            return 0
        if not hasattr(root, 'depth'):
            root.depth = 1;
        if root.right == None and root.left == None:
            return root.depth
        if root.left != None:
            root.left.depth = root.depth+1;
            queue.append(root.left)
        if root.right != None:
            root.right.depth = root.depth+1;
            queue.append(root.right)

        return self.minDepth(queue.pop(0), queue)


myRoot = TreeNode(1)
myRoot.left = TreeNode(2)
myRoot.right = TreeNode(3)
myRoot.left.left = TreeNode(4)
myRoot.right.right = TreeNode(5)
sol = Solution()

print(sol.minDepth(myRoot))
