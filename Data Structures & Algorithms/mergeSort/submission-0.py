# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        arr1 = self.mergeSort(pairs[:(len(pairs)//2)])
        arr2 = self.mergeSort(pairs[(len(pairs)//2):])

        return self.merge(arr1, arr2)

    def merge(self, arr1: List[Pair], arr2: List[Pair])-> List[Pair]:
        self.res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i].key > arr2[j].key:
                self.res.append(arr2[j])
                j += 1
            elif arr1[i].key < arr2[j].key:
                self.res.append(arr1[i])
                i += 1
            else:
                self.res.append(arr1[i])
                self.res.append(arr2[j])
                i += 1
                j += 1
        if not i >= len(arr1):
            for n in arr1[i:]:
                self.res.append(n)
        if not j >= len(arr2):
            for n in arr2[j:]:
                self.res.append(n)
        return self.res
