class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        b.f: get the product of all elements except nums[i] by running a nested loop and append to res array.
        This will take O(n^2) time where n is the len(nums), and constant space O(1)

        imporved (if division allowed): With one pass traversal, we can get product of all elems of the arr, and then 
        do a second pass and divide total product by nums[i] to get the product except nums[i] and append.
        This will take O(n + n) ~ O(n) where n is the len of nums, and space remains constant.

        Optimized (no division): if no division is allowed we can trade some space to retain O(n) time complexity.
        We can create two arrs of size n, one prefix product and one suffix product. We can then with a single pass,
        fill in both arrays and append products to that index (prefix and postfix). With a second pass, for each index
        we can calculate the product except that index by multplying the prefix and postfix products to that index and appending
        to res.
        This would be a O(n + n) ~ O(n) time complexity as well as O(n + n) ~ O(n) space complexity. 
        """
        products = []
        product_so_far = 1
        for num in nums:
            products.append(product_so_far)
            product_so_far *= num
        product_so_far = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= product_so_far
            product_so_far *= nums[i]
        return products