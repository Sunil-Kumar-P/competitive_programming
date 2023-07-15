// 387. First Unique Character in a String

// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

// Example 1:

// Input: s = "leetcode"
// Output: 0

// Example 2:

// Input: s = "loveleetcode"
// Output: 2

// Example 3:

// Input: s = "aabb"
// Output: -1

// Constraints:

//     1 <= s.length <= 105
//     s consists of only lowercase English letters.

#include <iostream>
#include <unordered_map>
using namespace std;

int firstUniqChar(string s) {
    unordered_map<char, int> charCount;
    
    // Count the occurrences of each character
    for (char c : s) {
        charCount[c]++;
    }
    
    // Find the first non-repeating character
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (charCount[c] == 1) {
            return i;
        }
    }
    
    return -1;
}

int main() {
    cout << firstUniqChar("leetcode") << endl;      // Output: 0
    cout << firstUniqChar("loveleetcode") << endl;  // Output: 2
    cout << firstUniqChar("aabb") << endl;           // Output: -1
    
    return 0;
}
