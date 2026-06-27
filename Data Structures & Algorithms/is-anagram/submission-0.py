class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        chars = defaultdict(int)
        for ch in s:
            chars[ch] += 1
        for ch in t:
            if not ch in chars or chars[ch] == 0:
                return False
            chars[ch] -= 1
        return True