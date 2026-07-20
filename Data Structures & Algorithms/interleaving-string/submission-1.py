class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        s1 = "aaa"
        s2 = "bb"
        s3 = "aba"
        3 pointers and s3's pointer mandates when and which other pointer to shift
        
        s1 = "aaa"
        s2 = "bxc"
        s3 = "xba"

        choices: if i1, i2, i3 ->
        1) if both s1[i1] == s2[i2] == s3[i3], then shift either once + shifting i3
        2) if ONLY s1[i1] == s3[i3], then shift i1 and i3
        3) if ONLY s2[i2] == s3[i3], then shift i2 and i3
        4) else (no match current index), then shift both i1 and i2 while keeping i3
        success condition is when we have matched all chars in s3, and pointer is now i3 == len(s3)

        at most make two decisions per index in s3.
        If len(s3) == n, then time comp would be O(2^n).
        Space comp: recursion call stack, which can grow up to the max height of all 3 lengths sums. O(n+m+k)
        """
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def recurse(i1,i2,i3):
            if i3 == len(s3) and i2 == len(s2) and i1 == len(s1):
                return True
            if (i1, i2, i3) in cache:
                return cache[(i1, i2, i3)]
            if i2 == len(s2) and i1 == len(s1):
                return False
            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2] == s3[i3]:
                cache[(i1, i2, i3)] = recurse(i1+1,i2,i3+1) or recurse(i1,i2+1,i3+1)
            elif i1 < len(s1) and s1[i1] == s3[i3]:
                cache[(i1, i2, i3)] = recurse(i1+1, i2, i3+1)
            elif i2 < len(s2) and s2[i2] == s3[i3]:
                cache[(i1, i2, i3)] = recurse(i1, i2+1, i3+1)
            else:
                return False
            return cache[(i1, i2, i3)]
        return recurse(0,0,0)
