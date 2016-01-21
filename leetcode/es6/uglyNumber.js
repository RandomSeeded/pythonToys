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
var isUgly = function(num) {
  var uglyFactors = {
    2: true,
    3: true,
    5: true
  }

  var hasNonUglyFactor = function(num) {
    var isPrime = true;
    for (var i = 2; i < num; i++) {
      if (num % i === 0) {
        isPrime = false;
        if (hasNonUglyFactor(num / i)) {
          return true;
        }
      }
    }
    if (isPrime && !uglyFactors[num]) { 
      return true;
    }
    return false;
  }

  return ! hasNonUglyFactor(num); 
}

console.log(isUgly(10));
console.log(isUgly(70));



