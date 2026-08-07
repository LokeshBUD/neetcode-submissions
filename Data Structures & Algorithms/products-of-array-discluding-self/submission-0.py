class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Basically, the idea here is that prefix product will take everything from the left of that index, multiply it, and store it at that index. 
        Postfix will take the right value, multiply it all, and store it at that index. That way, we are getting both sides of all the indices, 
        and that is the final result. 
        """
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
