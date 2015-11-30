# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Non-optimal solution: turn into sorted array
class Solution(object):
    def depthFirstArray(self, sortedArr, node):
        if node.left != None:
            self.depthFirstArray(sortedArr, node.left)
        sortedArr.append(node.val)
        if node.right != None:
            self.depthFirstArray(sortedArr, node.right)
        return sortedArr

    def kthSmallest(self, root, k):
        sorted = self.depthFirstArray([], root)
        print(sorted[k-1])
        return sorted[k-1]


myNode = TreeNode(1)
myNode.left = TreeNode(0)
myNode.right = TreeNode(2)
sol = Solution()
sol.kthSmallest(myNode, 1)
