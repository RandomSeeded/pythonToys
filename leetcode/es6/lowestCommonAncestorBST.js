// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

//  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
// 
// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
// 
//         _______6______
//        /              \
//     ___2__          ___8__
//    /      \        /      \
//    0      _4       7       9
//          /  \
//          3   5
// 
// For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
// 

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
// General thoughts/principle:
// If the node we're looking at is larger/smaller than both, there exists a better common ancestor.
var lowestCommonAncestor = function(root, p, q) {
  var curr = root;
  while ((curr.val < p.val && curr.val < q.val) 
      || (curr.val > p.val && curr.val > q.val)) {
    if (curr.val < p.val) {
      curr = curr.right;
    } else {
      curr = curr.left;
    }
  }
  return curr;
};

// root = new TreeNode(5);
// root.left = new TreeNode(3);
// root.right = new TreeNode(6);
// root.left.left = new TreeNode(2);
// root.left.right = new TreeNode(4);
// root.left.left.left = new TreeNode(1);
// console.log(lowestCommonAncestor(root, root.left.left.left, root.left.right));

root = new TreeNode(6);
root.left = new TreeNode(2);
root.right = new TreeNode(8);
root.left.left = new TreeNode(0);
root.left.right = new TreeNode(4);
root.right.left = new TreeNode(7);
root.right.right = new TreeNode(9);
root.left.right.left = new TreeNode(3);
root.left.right.right = new TreeNode(5);
console.log(lowestCommonAncestor(root, root.left.right.left, root.left.right.right));

