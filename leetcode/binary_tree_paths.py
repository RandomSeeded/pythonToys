# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Seems like a pretty straighforward dfs problem

class Solution(object):
    def binaryTreePaths(self, root):
        if root == None:
            return []
        paths = []
        def dfs(node, path = None):
            path = str(node.val) if path == None else path + "->"+str(node.val)
            print('path',path)
            # This is a root
            if node.left == None and node.right == None:
                paths.append(path)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root)
        return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
sol = Solution()
print(sol.binaryTreePaths(root))




