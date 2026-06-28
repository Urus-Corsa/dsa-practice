"""
my naive thought to solve this is to have the encode function traverse each string of strs and append each char to the 
final str that we wanna return and at the end of each str append a ",". 
If the len of strs is m (we have m strings) and the longest string is n chars long, the time it takes to generate
the final str is going to be O(m.n)
The space for encode function would be a the sum of the lenghts of all strings in str plus the ","s will be needed in between each word
so order of O(m.n)

For decode the same thing in reverse.

I am thinking we need to account for "," that are in the chars of the words as well, so using "," as a delimeter won't work when the strings
have "," as a char in them.
We need to come up with a strategy where we can have a delimeter that is a set and shared ruleset between the two functions
We can utilize the len of each str and append that at the begining of each str in the long str so that we iterate that many times
to get all the chars and then we go to the next. In order to know when the digits are part of the len or the word itself we can
append a #. So ["2hello1", "0worlD"] will be string = "7#2hello16#0worlD"
this way when we start, we turn all digits after the end of last string and before # into an int to make become our iterator
and then we get the next str

This way the time it takes will still be O(m.n)~O(sum of len of all strs) and the space needed would be O(sum of len of all strs in addition to the len and # digits which
are negligble compared to the overal size of the str) 
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(f"{len(string)}#{string}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            len_str = []
            while s[i] != "#":
                len_str.append(s[i])
                i += 1
            i += 1 #skip "#"
            length = int("".join(len_str))
            this_str = []
            while length != 0:
                this_str.append(s[i])
                i += 1
                length -= 1
            decoded.append("".join(this_str))
        return decoded