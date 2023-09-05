# 3. Write a function to validate if the provided two strings are anagrams or not. If the two strings
# are anagrams, then return ‘yes’. Otherwise, return ‘no’.
# Input:
# Input 1: 1st string
# Input 2: 2nd string
# Output:
# (If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)
# Example
# Input 1: Listen
# Input 2: Silent
# Output:
# Yes
# Explanation
# Listen and Silent are anagrams (an anagram is a word formed by rearranging the letters of the
# other word).

def IsAnagram(str1,str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if(len(str1)!=len(str2)):
        return "No"
    
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str2:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return "No"
    return "Yes"

print(IsAnagram("Listen", "Silent"))