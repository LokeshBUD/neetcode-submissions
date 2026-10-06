class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store idx of value in hm, get diff and check hm if there get value else return []
        hm = defaultdict(int)
        
        for i,num in enumerate(nums):
            diff = target - num
            if diff in hm:
                return [hm[diff], i]
            hm[num] = i
        return []
        
       
        
            

                