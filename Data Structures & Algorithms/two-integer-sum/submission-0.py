class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}
        # pos = []

        # for i,v in enumerate(nums):
        #     #check[target-v] = check.get(target,0)
        #     if target-v in nums:
        #         check[v] = check.get(v,i)

        # return list(check.values())


        for index,value in enumerate(nums):
            if target-value in check:
                return [check[target-value], index]

            check[value] = check.get(value, index)
