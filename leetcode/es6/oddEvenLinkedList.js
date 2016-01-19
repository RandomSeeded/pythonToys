// https://leetcode.com/problems/odd-even-linked-list/

// Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
// 
// You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
// 
// Example:
// Given 1->2->3->4->5->NULL,
// return 1->3->5->2->4->NULL.
// 
// Note:
// The relative order inside both the even and odd groups should remain as it was in the input.
// The first node is considered odd, the second node even and so on ... 

// So: we want to have all the odd nodes first, then the even nodes
// Easiest way to do this would be to NOT do it in place, and just have two LLs. Then append the even onto the odds. This actually IS O(1) space and O(N) time.
// How else could we do it? We do the same thing-ish, and just have pointers to last-even and last-odd


// Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}

var oddEvenList = function(head) {
  var curr = head;
  var evenhead;
  var odd;
  var even;
  var counter = 1;
  while (curr !== null) {
    var nextUp = curr.next;
    // Initialize odd and even lls
    if (counter === 1) {
      odd = curr;
      curr.next = null;
    } else if (counter === 2) {
      even = curr;
      evenhead = curr;
      curr.next = null;
    } else {
      if (counter % 2 === 1) {
        odd.next = curr;
        odd = curr;
      } else {
        even.next = curr;
        even = curr;
      }
    }
    curr = nextUp;
    counter++;
  }
  if (odd) {
    odd.next = evenhead || null;
  }
  if (even) {
    even.next = null;
  }
  return head;
};

root = new ListNode(0);
root.next = new ListNode(1);
root.next.next = new ListNode(2);
root.next.next.next = new ListNode(3);
root.next.next.next.next = new ListNode(4);
// root.next.next.next = new ListNode(4);
// root.next.next.next.next = new ListNode(5);
// root.next.next.next.next.next = new ListNode(6);
// root.next.next.next.next.next.next = new ListNode(7);
// root.next.next.next.next.next.next.next = new ListNode(8);

console.log(oddEvenList(root).next.next.next);

