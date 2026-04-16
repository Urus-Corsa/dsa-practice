class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSum to be initialized with the first possible 
        # subarray's maximum sum since this constraint exists
        # 1 <= nums.length <= 1000
        maxSum = nums[0]
        # curSum to keep track of the sum of the subarray being looked at
        curSum = 0

        #i terating over nums to look at subarray sums
        for i in nums:
            # check to see if the curSum has become negative since
            # elems can be negative, if so reset it back to zero.
            # this means that whatever subarray sum that has become negative
            # will not help increasing the sum since we are looking for the max sum
            curSum = max(curSum, 0)
            # add this elem to the count of subarrays until this elem
            curSum += i
            # if curSum has become larger the maxSum ever seen, have maxSum
            # keep a record of this largest that was found
            maxSum = max(maxSum, curSum)
        
        # return the maxSum ever recorded
        return maxSum