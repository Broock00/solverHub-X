class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        if val == val[::-1]:
            return True
        return False
