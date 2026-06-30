class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        b.f: compare each elem, O(n^2) time and O(1) space, inefficient
        improved: make a dict of numm elems as keys and their indecies into a list, taverse nums, searching for presence of the target-nums[i],
        if found, we ensure current index is not the same as the index of the complement if not we return the indecies. If they are we continue to find the answer. This takes O(n) time to populate dict, and O(n) to traverse nums searching for the complement, so O(2n)~O(n) time total
        The space it needs will be for the dict which will have u keys where u is the len(set(nums)) aka unique elems in nums and the indecies list could grow as large as the len(nums) in total. O(u+n) where n dominates here so O(n)
        optimal: Same approach but we do it in one pass. We initialize dict to defaultdict(list) and at each iter of nums check for complement's presence in dict, if it is then we grab its index and current index and return
        This will faster by a factor O(n) compared to the O(2n) of the improved solution
        """
        seen = defaultdict(list)
        for i,num in enumerate(nums):
            if target-num in seen:
                return [min(i,seen[target-num][0]), max(i,seen[target-num][0])]
            seen[nums[i]].append(i)