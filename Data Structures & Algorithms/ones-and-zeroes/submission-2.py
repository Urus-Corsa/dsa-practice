class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        char_count = defaultdict(tuple)
        for i, str in enumerate(strs):
            zeros = 0
            ones = 0
            for ch in str:
                if ch == '0':
                    zeros += 1
                else:
                    ones += 1
            char_count[i] = (zeros, ones)
        cache = {}
        def recurse(curr_i, zeros_count, ones_count):
            if (curr_i, zeros_count, ones_count) in cache:
                return cache[(curr_i, zeros_count, ones_count)]
            if curr_i >= len(strs) or zeros_count > m or ones_count > n:
                return 0
            include = 0
            i_zeros, i_ones = char_count[curr_i]
            if i_zeros+zeros_count <= m and i_ones+ones_count <= n:
                include = 1 + recurse(curr_i+1, zeros_count+i_zeros, i_ones+ones_count)
            exclude = recurse(curr_i+1, zeros_count, ones_count)
            cache[(curr_i, zeros_count, ones_count)] = max(include, exclude)
            return cache[(curr_i, zeros_count, ones_count)]
        return recurse(0,0,0)
