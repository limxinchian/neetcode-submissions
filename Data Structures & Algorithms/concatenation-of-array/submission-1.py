class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # solution 1 
        # return nums + nums

        # solution 2
        ans = []

        for i in range (2):
            for num in nums:
                ans.append(num)
        return ans

