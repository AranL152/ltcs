class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        me = {}

        for i, num in enumerate(nums):
            if (target-num) in me:
                ret.append(i)
                ret.append(me[target-num])
            me[num] = i
        
        return ret