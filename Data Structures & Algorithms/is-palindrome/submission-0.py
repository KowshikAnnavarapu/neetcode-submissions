class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        reverse = new[::-1]
        if reverse == new:
            return True
        else:
            return False

        