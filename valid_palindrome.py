def isPalindrome(self, s):
        s = s.lower()
        clean_text = ''.join(char for char in s if char.isalnum())
        left = 0
        right = len(clean_text)-1

        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1
        return True