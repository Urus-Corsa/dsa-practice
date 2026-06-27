class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        brute force: 
        Create a hash map and iterate over strs and append the index of each str to the sorted str key in the hashmap (sort each str, and use it as a key in the hashmap)
        This means to call sort on every str. So if m strings in strs, then it'd take m(nlogn) where n is the len of each str.
        Then we can iterate over the items of strs, and append all values in strs at indecies of each key into the result array as a separate inner array.

        Time to fill in the hash map or dict will be O(m(nlogn)) where m is the number of strings in strs and n is the len of the longest str (in the worst case).
        Then we need to iterate over the hash map (which its size is as large as the strs array itself in the worst case where each sorted string is different) and append the indecies to the result array.

        So total time it takes in the worst case is O(2.m(nlogn)) ~ O(m(nlogn))
        and the space is O(m) for the hashmap and O(m) for the res array so simplified is O(m)
        """
        res = []
        sorted_keys = defaultdict(list)
        for string in strs:
            sorted_keys["".join(sorted(string))].append(string)
        for key, strings in sorted_keys.items():
            res.append(strings)
        return res