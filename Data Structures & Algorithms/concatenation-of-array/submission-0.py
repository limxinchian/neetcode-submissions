class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums += nums
        # return nums
        for num in range (len(nums)):
            nums.append(nums[num])
        
        return nums