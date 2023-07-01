import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class valid_anagram {
    public boolean isAnagram(String s, String t) {
        // Check if the lengths of the two strings are equal
        if (s.length() != t.length()) return false;

        // Create an integer array called 'store' to keep track of character counts
        int[] store = new int[26];

        // Iterate over each character in both strings
        for (int i = 0; i < s.length(); i++) {
            // Increment the count for the character in string 's'
            store[s.charAt(i) - 'a']++;
            // Decrement the count for the character in string 't'
            store[t.charAt(i) - 'a']--;
        }

        // Iterate over the 'store' array to check if any character counts are non-zero
        for (int n : store) {
            // If a non-zero count is found, the strings are not anagrams
            if (n != 0) return false;
        }

        // If all character counts are zero, the strings are anagrams
        return true;
    }
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s, t;
        try {
            s = reader.readLine();

            t = reader.readLine();

            valid_anagram solution = new valid_anagram();
            boolean isAnagram = solution.isAnagram(s, t);

            System.out.println(isAnagram);
            
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}