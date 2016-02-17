// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

// Given a linked list, remove the nth node from the end of list and return its head.
// 
// For example,
// 
//    Given linked list: 1->2->3->4->5, and n = 2.
// 
//    After removing the second node from the end, the linked list becomes 1->2->3->5.
// 
// Note:
// Given n will always be valid.
// Try to do this in one pass. 

// THOUGHTS:
// 1) could store references to all the nodes. Space intensive, clearly, but easily one pass
// 2) 2 passes to figure out which node to remove
// If we knew specifically which node we wanted to remove, we could do that in constant time
// But the crux of this question is: how do we know which one we want to remove?
// I think the best way to do that would be to have a queue of size n

function ListNode(val) {
    this.val = val;
    this.next = null;
}

function Queue(size) {
  this.storage = {};
  this.start = 0;
  this.end = 0;
  this.size = size;

  this.add = function(val) {
    this.storage[this.end++] = val;
    if (this.end - this.start > this.size) {
      delete this.storage[this.start++];
    }
  }
  this.getNthFromLast = function() {
    return this.storage[this.start];
  }
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  var curr = head;
  var Q = new Queue(n);
  while (curr !== null) {
    Q.add(curr);

    curr = curr.next;
  }
  var nthFromEnd = Q.getNthFromLast();
  if (nthFromEnd.next) {
    nthFromEnd.val = nthFromEnd.next.val;
    nthFromEnd.next = nthFromEnd.next.next;
  } else {
    nthFromEnd = null;
  }
    
  return head;
};

start = new ListNode(1);
// console.log(removeNthFromEnd(start, 1));
start.next = new ListNode(2);
start.next.next = new ListNode(3);
start.next.next.next = new ListNode(4);
start.next.next.next.next = new ListNode(5);
console.log(removeNthFromEnd(start, 2));


