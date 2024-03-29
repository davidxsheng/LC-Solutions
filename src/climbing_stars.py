import functools


class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
