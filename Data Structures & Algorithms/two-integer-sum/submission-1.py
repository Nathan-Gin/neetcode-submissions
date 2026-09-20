class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in seen:
                return [seen[pair], i]
            seen[nums[i]] = i