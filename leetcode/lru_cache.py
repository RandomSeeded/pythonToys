# https://leetcode.com/problems/lru-cache/
# Let's think about this
# We have a few things we want this data structure to be able to do
# GET & SET. Ideally in as fast a time as possible, which suggests hashing algorithm
# HOWEVER, we also want to remove (?) items when a certain capacity is reached
# The problem with hashing is that in order to remove the oldest, we would need to find the oldest to remove it
# Could we do a dual data structure, with both a hash and a queue? Perhaps! One thing that makes this nice is there's no removal of items.
# Let's try

import collections
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.q = collections.deque([],capacity)
        """
        :type capacity: int
        """

    def get(self, key):
        # note: getting counts as accessing for purposes of lru
        if key in self.storage:
            self.q.remove(key)
            self.q.append(key)
            return self.storage[key]
        else:
            return -1
        """
        :rtype: int
        """
        

    def set(self, key, value):
        # There's one special case we need to handle: what if the key is already present?
        if key in self.storage:
            self.q.remove(key)

        if len(self.q) == self.capacity:
            key_to_remove = self.q.popleft()
            print('reached, removing', key_to_remove)
            del self.storage[key_to_remove]
        self.q.append(key)
        self.storage[key] = value

        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

lc = LRUCache(2)
lc.set(2,1)
lc.set(2,2)
print(lc.get(2))
lc.set(1,1)
lc.set(4,1)
print(lc.get(2))
print(lc.get(1))

