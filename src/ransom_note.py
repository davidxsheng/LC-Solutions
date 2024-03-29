import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = collections.Counter(ransomNote)
        magazine_letters = collections.Counter(magazine)
        for letter, frequency in ransom_letters.items():
            magazine_frequency = magazine_letters.get(letter, 0)
            if magazine_frequency < frequency:
                return False
        return True
