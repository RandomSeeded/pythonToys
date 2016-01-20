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
var countPrimes = function(n) {
  var seen = {};

  var helperPrimes = function(n, results) {
    results = results || 0;
    if (seen[n]) {
      return seen[n];
    }
    var isPrime = true;
    for (var i = 2; i <= Math.floor(n/2); i++) {
      var remainder = n % i;
      if (remainder === 0) {
        results += helperPrimes(n / i);
        isPrime = false;
      }
    }
    if (isPrime) {
      results++;
    }
    seen[n] = results;
    return results;
  }

  return helperPrimes(n);
}

console.log(countPrimes(7));
console.log(countPrimes(8));
console.log(countPrimes(16));
