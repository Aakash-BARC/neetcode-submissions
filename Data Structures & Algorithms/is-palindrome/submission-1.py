class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_string=""
        for i in s.lower():
            if i in 'abcdefghijklmnopqrstuvwxyz1234567890':
                converted_string = converted_string + i

        return converted_string == converted_string[::-1]