// https://leetcode.com/problems/count-primes/
// Description:
// 
// Count the number of prime numbers less than a non-negative number, n.

// THOUGHTS:
// Dynamic programming (hash of results) + check for every num within it


/**
 * @param {number} n
 * @return {number}
 */

// ES5
// This time actually solving the problem being asked. How many primes BELOW a certain #?
// AKA 
var countPrimes = function(n) {
  function isPrime(n) {
    for (var i = 2; i <= Math.floor(n/2); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }

  var results = 0;
  for (var i = 2; i < n; i++) {
    if (isPrime(i)) {
      results++;
    }
  }
  return results;
}

console.log(countPrimes(7));
console.log(countPrimes(8));
console.log(countPrimes(16));

// var countPrimes = function(n) {
//   var seen = {};
// 
//   var helperPrimes = function(n, results) {
//     results = results || 0;
//     if (seen[n]) {
//       return seen[n];
//     }
//     var isPrime = true;
//     for (var i = 2; i <= Math.floor(n/2); i++) {
//       var remainder = n % i;
//       if (remainder === 0) {
//         results += helperPrimes(n / i);
//         isPrime = false;
//       }
//     }
//     if (isPrime) {
//       results++;
//     }
//     seen[n] = results;
//     return results;
//   }
// 
//   return helperPrimes(n);
// }

