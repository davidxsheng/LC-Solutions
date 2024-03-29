def preprocess_string(s: str) -> str:
    """Strips whitepsace, converts to lowercase, and removes non-alphanumeric characters.

    Args:
        s (str): The string to preprocess.

    Returns:
        str: The preprocessed string.
    """
    return "".join(char.lower() for char in s if char.isalnum())


class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocessed_s = preprocess_string(s)
        right = len(preprocessed_s) - 1
        left = 0
        for _ in range(len(preprocessed_s) // 2):
            if preprocessed_s[left] != preprocessed_s[right]:
                return False
            left += 1
            right -= 1
        return True
