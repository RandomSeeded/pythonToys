// https://leetcode.com/problems/ugly-number/
//
// Write a program to check whether a given number is an ugly number.

// Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
// 
// Note that 1 is typically treated as an ugly number. 

/**
 * @param {number} num
 * @return {boolean}
 */

// New approach: remove all factors 2, 3, and 5, then see if there are any other prime factors
var isUgly = function(num) {
  var uglyFactors = {
    2: true,
    3: true,
    5: true
  };

  // If all factors were ugly, it's ugly
  if (num === 1) {
    return true;
  } else if (num === 0) {
    return false;
  }

  for (var factor in uglyFactors) {
    // If there are any ugly factors, remove and recurse
    if (num % factor === 0) {
      return isUgly(num / factor);
    } 
  }
  // Otherwise, we have a non-ugly number
  return false;
};

// This version works (I believe) but is too slow
// var isUgly = function(num) {
//   var uglyFactors = {
//     2: true,
//     3: true,
//     5: true
//   }
// 
//   var hasNonUglyFactor = function(num) {
//     var isPrime = true;
//     for (var i = 2; i <= Math.sqrt(num); i++) {
//       if (num % i === 0) {
//         isPrime = false;
//         if (hasNonUglyFactor(num / i)) {
//           return true;
//         }
//       }
//     }
//     if (isPrime && !uglyFactors[num]) { 
//       return true;
//     }
//     return false;
//   }
// 
//   return ! hasNonUglyFactor(num); 
// }

console.log(isUgly(4));
console.log(isUgly(10));
console.log(isUgly(20));
console.log(isUgly(14));
console.log(isUgly(70));
console.log(isUgly(905391974));
console.log(isUgly(2123366400));




