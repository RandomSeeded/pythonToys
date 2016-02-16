// https://leetcode.com/problems/valid-anagram/

// Given two strings s and t, write a function to determine if t is an anagram of s.
// 
// For example,
// s = "anagram", t = "nagaram", return true.
// s = "rat", t = "car", return false.
// 
// Note:
// You may assume the string contains only lowercase alphabets.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  // If they don't have the same amount of characters, can't be anagrams
  if (s.length !== t.length) {
    return false;
  }

  // Otherwise, check to see if the letter counts are the same
  counts = {};
  countt = {};
  for (var i = 0; i < s.length; i++) {
    counts[s[i]] = (counts[s[i]] || 0) + 1;
    countt[t[i]] = (countt[t[i]] || 0) + 1;
  }
  for (var letter in counts) {
    if (counts[letter] !== countt[letter]) {
      return false;
    }
  }
  return true;
}


console.log(isAnagram('anagram','nagaram'));
console.log(isAnagram('rat','car'));

