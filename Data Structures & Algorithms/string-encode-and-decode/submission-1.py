class Solution:
    """
    we need to design two functions where one takes in a list of strings and encodes the entire list into a single str and returns it
    and the other takes the encoded string and decodes it back to the original list of strings

    Clarifications:
    1. will the list of strs always be valid?
    2. what type of characters do we expect to see? alphabets (lower? upper? both?), numeric, special chars?
    3. can the list ever be empty?
    4. any change the decode functions receives a curropted version? Will it always receive the same exact output?
    5. limit of the list len, and longest str len?

    approaches:
    the brute force way of solving is to just go through chars of each str, and append each char to the encoded str. At the end of
    each string we can have an indicator that will basically put a separation there meaning that string has ended and we should start
    a new string when decoding. We could use , or any other special character or even character but there is no way to tell whether
    that char itself is part of the original str or not when decoding
    so instead, what we can do is to have the len of each string with an hash sign(or any other indicator) before we append the chars to the
    encoded str so that when we decode we use the len as the source of truth to know how many chars after the special sign we need to consider 
    for this str.

    Time:
    encode: we need to traverse all strings in strs list to append their len, separator, and chars to the res str.
    If we know the len of all str are at their max cap and is m and there are n strings in strs then time needed to do this would O(n.m) in the worst case and 
    at the end we will run .join() on all strs which would be take as long as count of chars in final str which would be around O(n.m)
    So total time is O(2(m.n)) ~ O(m.n)
    space needed would be an array of size O(n.m) to store the lengths and strs to run .join on at the end and another O(n.m) for the final str
    so space comp also is O(2(n.m)) ~ O(n.m)

    decode: we need to traverse the entire str to decode, it will take us pretty much the same time and space as encode O(n.m)
    """
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)))
            encoded.append("#")
            encoded.append(string)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i<len(s):
            length = []
            while s[i].isnumeric():
                length.append(s[i])
                i += 1
            i += 1 #bypass the #
            length = int("".join(length))
            string = []
            while length != 0:
                string.append(s[i])
                i += 1
                length -= 1
            decoded.append("".join(string))
        return decoded







