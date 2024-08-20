from re import findall


class Solution:
    def is_palindrome(self, phrase: str) -> bool:
        forwards = ''.join(findall(r'[a-z]+', phrase.lower()))
        backwards = forwards[::-1]

        return forwards == backwards