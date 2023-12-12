class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Using a dictionary to store indices of numbers
        for i, num in enumerate(nums):
            diff = target - num # 9-2 = 7
            if diff in num_indices:
                return [num_indices[diff], i] # {0, 1}
            num_indices[num] = i # {2,0}
        return []
