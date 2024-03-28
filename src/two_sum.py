class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        candidates = dict()
        for idx, num in enumerate(nums):
            if num in candidates:
                return [candidates[num], idx]
            else:
                candidates[target - num] = idx
        return [-1, -1]
