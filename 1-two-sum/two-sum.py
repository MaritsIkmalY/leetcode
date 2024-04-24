class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for index, value in enumerate(nums):
            if target - value in result:
                return [index, result[target - value]]
            result[value] = index