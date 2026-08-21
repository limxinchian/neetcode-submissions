class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_dict = {}

        for index,num in enumerate(nums):
            if target-num in pos_dict:
                return [pos_dict[target-num], index]

            pos_dict[num] = index