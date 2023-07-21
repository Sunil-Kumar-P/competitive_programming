// 125. Valid Palindrome

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.
 
// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.

// Example 2:
// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.

// Example 3:
// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.

// Constraints:

var isPalindrome = function(s) {
    const isAlphanumeric = (char) => {
        const charCode = char.charCodeAt(0);
        return (charCode >= 48 && charCode <= 57) || // Numbers
            (charCode >= 65 && charCode <= 90) || // Uppercase letters
            (charCode >= 97 && charCode <= 122); // Lowercase letters
    };
    let cleanedStr = '';
    for (let i = 0; i < s.length; i++) {
        if (isAlphanumeric(s[i])) {
            cleanedStr += s[i].toLowerCase();
        }
    }
    let i = 0;
    let j = cleanedStr.length - 1;
    while (i < j) {
        if (cleanedStr[i] !== cleanedStr[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));