class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        brute force, go through all substr staring with each char (O(n^2)) and for each run a 2-pointer inwards for palindrome
        check and return max len calculated. Len of longest substr == len(s) (s itself as substr) so the time comp is O(n^3)
        Space comp if we dont store the substrs is O(1), and if we stored all substrs (we would have O(n(n+1)/2)) ~ O(n^2), if 
        we dont store it's O(1)
        We can come up with a bit of an intuitive approach, and assume that each char is the middle of a substr and go outwards with
        two pointers until there is a mismatch (palindromic property breaks), and keep track of longest len seen. This works with palindromes
        of odd len like "aba", for even len palindroms like bccb, we can imagine curr_i and curr_i are the middle indecies (only if they are equal)
        and if so then extend outwards from each while keeping track of max len seen. 
        """
        count = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l>=0 and r<len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
