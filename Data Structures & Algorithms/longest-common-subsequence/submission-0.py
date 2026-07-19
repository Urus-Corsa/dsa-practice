class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def recurse(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            matched = 0
            branch_shifting = 0
            if text1[i1] == text2[i2]:
                matched = 1 + recurse(i1+1, i2+1)
            else:
                branch_shifting = max(recurse(i1+1, i2), recurse(i1, i2+1))
            cache[(i1, i2)] = max(branch_shifting, matched)
            return cache[(i1, i2)]
        return recurse(0,0)
            
