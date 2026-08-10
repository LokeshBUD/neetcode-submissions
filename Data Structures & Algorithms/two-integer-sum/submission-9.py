class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store idx of value in hm, get diff and check hm if there get value else return []
        hm = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hm:
                return[hm[diff], i]
            hm[n] = i
            
        return []
            

                