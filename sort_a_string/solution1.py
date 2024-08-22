class Solution:
    def sort_string(self, s):
        return ' '.join(sorted(s.split(), key=lambda s: str.casefold))