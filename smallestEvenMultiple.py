class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(n):
            if 2 * i == n:
                return n
        return 2 * n
