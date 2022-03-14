"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, 
such that there is a bijection between a letter in pattern 
and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
# Filename: 290_word_pattern.py
# Description: https://leetcode.com/problems/word-pattern/
# Author: Rajesh Pyne
# Email:  rajesh.pyne@gmail.com

# Approach
# Check1 : if the length of pattern and s is not matching,
#           then return False,
#           else proceed to check2
# Check2 : get each alphabet set and word set from pattern and zip the two list to get a tuple set
#           and find out the length of each set, if the length of all set matches, then True


def word_pattern(pattern: str, s: str) -> bool:
    pattern_len = len(pattern)
    # print(pattern_len)
    s_len = len(s.split(" "))
    # print(s_len)

    if pattern_len != s_len:
        return False

    char_pattern = [a.lower() for a in pattern]
    # print(char_pattern)
    word_s = [x.strip().lower() for x in s.split(" ")]
    # print(word_s)
    tuple_list = list(zip(char_pattern, word_s))
    # print(set(tuple_list))
    # print(len(set(char_pattern)), len(set(word_s)), len(set(tuple_list)))
    if len(set(char_pattern)) == len(set(word_s)) == len(set(tuple_list)):
        return True
    else:
        return False


n = word_pattern("abba", "dog cat cat dog")
assert n == True, "Output not matching"
n = word_pattern("abba", "dog cat cat fish")
assert n == False, "Output not matching"
n = word_pattern("aaaa", "dog cat cat dog")
assert n == False, "Output not matching"

print("All Test cases Passed")
