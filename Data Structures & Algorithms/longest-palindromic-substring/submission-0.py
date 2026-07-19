class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        this problem means that for any substring of s we need to check whether it's a palindrome or not and if it is record
        it's length. At the end return the palindrome substring that has maximum len
        One approach that comes to mind is that we can brute force this by generating all substrings of s (O(n^2) time) and O(n(n+1)//2)~O(n^2)
        then for each substring we can use 2 pointers to detect whether they are palindromes O(n) for each substr, if it is palindrome
        and len is highest that max seen so far we update, else we move on.
        
        optimized: consider every char the middle substr of a supposed palindrome, and shift outwards until there is a mismatch between the two pointers.
        This works well for palindromes of odd size, and for even size palindrome like "abba" we can first check to see if the next char is equal to curr char
        if so, then these two could be the middle chars of an even len palindromic substr, so we repeat the same process of going outwards with two pointers
        If inequal, then we break that loop. We can update our maximum as we go as well.
        """
        max_len_substr = (None, 0)
        for i in range(len(s)):
            l, r = i,i
            max_len_so_far = max_len_substr[1]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len_so_far:
                    max_len_substr = (s[l:r+1], r-l+1)
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len_so_far:
                    max_len_substr = (s[l:r+1], r-l+1)
                l -= 1
                r += 1
        return max_len_substr[0]