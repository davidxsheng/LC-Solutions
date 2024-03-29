class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left 