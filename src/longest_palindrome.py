import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindrome_length = 0
        char_frequencies = collections.Counter(s)
        has_odd_frequency_char = False
        for frequency in char_frequencies.values():
            if frequency % 2:
                has_odd_frequency_char = True
                palindrome_length += frequency - 1
            else:
                palindrome_length += frequency
        return palindrome_length + has_odd_frequency_char

