class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            idx[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx and idx[diff] != i:
                return [i, idx[diff]]
        return []

        