class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        count = 0
        
        for num in nums:
            if num - 1 not in numsSet:
                curr_num = num
                curr_count = 1
                while curr_num+1 in numsSet:
                    curr_count += 1
                    curr_num += 1
                count = max(curr_count, count)
        return count
