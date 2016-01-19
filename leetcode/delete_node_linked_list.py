# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# 
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
# 
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
    	if self.next:
		return str(self.val) + str(self.next)
	else:
		return str(self.val)

# OK SO HERE'S THE DEAL
# We have no ability to modify the previous pointer to the next pointer, b/c we don't even have axx to the root
# SO, the way we can go about this is by looping through all remaining nodes, and editing them to have the next value in line
class Solution(object):
    def deleteNode(self, node):
    	while node.next:
		node.val = node.next.val
		if not node.next.next:
			node.next = None
		else:
			node = node.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
sol = Solution()
sol.deleteNode(root.next)
print(root)



        
