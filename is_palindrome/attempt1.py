class Solution:
    def is_palindrome(self, phrase: str) -> bool:
        only_letters = ''
        for letter in phrase.upper():
            if ord(letter) >= 65 and ord(letter) <= 90:
                only_letters += letter
        
        return only_letters == only_letters[::-1]