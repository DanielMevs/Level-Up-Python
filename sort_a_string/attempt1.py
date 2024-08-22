class Solution:
    def sort_string(self, s):
        return ' '.join(sorted(s.split(), key=lambda s: s.lower()[0]))