// https://leetcode.com/problems/rotate-array/
// Rotate an array of n elements to the right by k steps.
// 
// For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
// 
// Note:
// Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem. 


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// Easiest possible method ever
var rotate = function(nums, k) {
  var copied = nums.slice();
  var shiftAmount = k % nums.length;
  console.log(shiftAmount);
  for (var i = 0; i < nums.length; i++) {
    // nums[i] = copied[i+shiftAmount+1];
    nums[i] = (i + shiftAmount + 1 >= nums.length) ? copied[i-shiftAmount] : copied[i+shiftAmount+1];
  }
}

var nums = [1,2,3,4,5,6,7];
rotate(nums,3);
console.log(nums);
