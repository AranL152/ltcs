class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        check = {}

        for i, num in enumerate(nums):
            if (target-num) in check:
                ret.append(i)
                ret.append(check[target-num])
            check[num] = i
        
        return ret