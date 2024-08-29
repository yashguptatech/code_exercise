class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Checks if an integer is a palindrome without converting to string.

        Args:
            x: The integer to check.

        Returns:
            True if x is a palindrome, False otherwise.
        """

        if x < 0:
            return False

        reversed_number = 0
        original_number = x

        while x > 0:
            reversed_number = (reversed_number * 10) + (x % 10)
            x //= 10

        return reversed_number == original_number