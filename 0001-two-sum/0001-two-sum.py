class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            need_num = target - num 
            if need_num in seen:
                return [seen[need_num], index]
            seen[num] = index  
        return []



