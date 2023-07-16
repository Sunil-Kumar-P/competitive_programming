// 242. Valid Anagram

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true

// Example 2:

// Input: s = "rat", t = "car"
// Output: false

// Constraints:

//     1 <= s.length, t.length <= 5 * 104
//     s and t consist of lowercase English letters.
// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

#include <iostream>
#include <unordered_map>

using namespace std;
bool isAnagram(string s, string t) {
    if (s.length() != t.length()) {
        return false;
    }
    unordered_map<char, int> store;

    for (char c : s) {
        store[c]++;
    }
    for (char c : t) {
        if (store.find(c) == store.end() || store[c] == 0) {
            return false;
        }
        store[c]--;
    }
    return true;
}

int main() {
    string s = "anagram";
    string t = "nagaram";
    cout << isAnagram(s, t) << endl;  // Output: 1 (true)

    s = "rat";
    t = "car";
    cout << isAnagram(s, t) << endl;  // Output: 0 (false)

    return 0;
}
