class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = []
        for i, num in enumerate(nums):
            nums_copy.append((num, i))
        nums_copy.sort()
        i, j = 0, len(nums)-1
        while i != j:
            curr = nums_copy[i][0]+nums_copy[j][0]
            if curr == target:
                return [min(nums_copy[i][1], nums_copy[j][1]), max(nums_copy[i][1], nums_copy[j][1])]
            if curr > target:
                j -= 1
            else:
                i += 1
        