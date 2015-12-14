# https://leetcode.com/problems/sort-list/
# Sort a linked list in O(n log n) time using constant space complexity.

# note: whether it's a LL or an array is pretty irrelevant. We could simply make a temp array and sort that
# Constant-space? We might be able to make this work with merge-sort, but could be a bit of a pain. What about quicksort?

# QUICKSORT STEPS:
# 1) pick a pivot (we'll just pick first element in the array)
# 2) put everything lower than pivot before pivot
# - how can we make this efficient? This is sort of the crux of the problem, doing this in-place.
# 3) put everything higher than pivot after pivot

# WE CAN TOTALLY JUST QS ON THE LL DIRECTLY
# In fact, it may be easier
# We pick pivot (head)
# We iterate through the list
# If something comes before the pivot, we INSERT it between the head and our node
# Otherwise, we leave it in place and continue iteration
# (No, it probably won't be easier)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        temp = self
        result = ""
        while (temp != None):
            result += str(temp.val) + ","
            temp = temp.next
        return result

class Solution(object):
    def sortList(self, start, end = None):
        # If 1 or 0 elements in our list, return
        if start == end:
            return

        # Initializations
        pivot = start
        current = start
        head = start

        while (current != end):
            current = current.next
            print('current.val', current.val)
            print('pivot.val', pivot.val)
            if current.val < pivot.val:
                print('need swap')


        return start

# class Solution(object):
#     def sortList(self, pivot, ending = None):
#         print('input', pivot)
#         if pivot == None or pivot.next == None or pivot == ending:
#             return pivot
# 
#         # Use anySwaps to figure out when the list is entirely sorted. Has the advantage of potentially short-cutting early if we manage to sort ahead of time
#         anySwaps = False
#         head = pivot
#         current = pivot
#         prev = None
# 
#         while (current != ending):
#             nextNode = current.next
# 
#             # If the current element should fall before the pivot
#             if current.val < pivot.val:
#                 # Insert it at the head
#                 if prev:
#                     prev.next = nextNode
#                 current.next = head
#                 head = current
#                 anySwaps = True
# 
#             # If it shouldn't, iterate the 2nd-to-current (prev)
#             else:
#                 prev = current
# 
#             # Iterate to look at the next node
#             current = nextNode
# 
#         print('first half', self.sortList(head, pivot))
#         print('second half', self.sortList(pivot.next, ending))
#         print('head', head)
# 
#         # The idea is that the sorts should have made it so everything following the head is correctly sorted. HOWEVER. Note that it's possible the head wasn't the 'true' head. Is that's what's going on?
#         return head

head = ListNode(4)
head.next = ListNode(9)
head.next.next = ListNode(8)
head.next.next.next = ListNode(5)
sol = Solution()
print(sol.sortList(head))

