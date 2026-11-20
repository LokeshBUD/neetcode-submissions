class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo,hi = 0, len(numbers) - 1
        while lo < hi:
            summ = numbers[lo] + numbers[hi]
            if summ == target:
                return [lo+1,hi+1]
            elif summ > target:
                hi -= 1
            else:
                lo += 1
        