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

import java.util.HashMap;
import java.util.Map;

public class firstUniqCharacter {
    public int firstUniqChar(String s) {
        Map<Character, Integer> charCount = new HashMap<>();
        
        // Count the occurrences of each character
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        // Find the first non-repeating character
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (charCount.get(c) == 1) {
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        firstUniqCharacter solution = new firstUniqCharacter();
        
        System.out.println(solution.firstUniqChar("leetcode"));      // Output: 0
        System.out.println(solution.firstUniqChar("loveleetcode"));  // Output: 2
        System.out.println(solution.firstUniqChar("aabb"));           // Output: -1
    }

}
