class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
        
        Approaches: 
        1. b.f: for each elem, we can multiply ever other elems and append to res arr.
        time for this will be O(n^2) if len(nums) = n, and space would be constant if not counting res arr else it'd be o(n) as well
        2. if division allowed: get total product in one pass to nums. In second pass to nums divide the total product by the elem and append results to res arr
        Time O(n) for total product pass + O(n) for division pass = O(2n) ~ O(n), space would be constant if not counting res arr else O(n)
        3. if division not allowed: with trade off of some space we can achieve O(n) w/o division. If we did a reverse traversal on nums and appended the product until each elem to the an arr,
        and then did a second traversal from begining, and kept track of a var that holds prefix product to that point we can get total product from elems before (var) and after (the arr) and append to res
        Time it takes would be a pass for postfix product fill in o(n) and second pass to populate res and get curr product.
        Space traded here is to maintain that postfix product arr o(n) if not counting res, else O(2n) which is still simplified to O(n)
        [1,3,5,10]
        [150,50,10,1]
        """
        postfix_products = [1 for i in range(len(nums))] #[1,1,1,1]
        for i in range(len(nums)-2, -1, -1):
            postfix_products[i] = postfix_products[i+1] * nums[i+1] #[150,50,10,1]
        prefix_product = 1
        res = []
        for i in range(len(nums)):
            res.append(prefix_product*postfix_products[i]) #[150, 50, 30, 15]
            prefix_product *= nums[i]
        return res
