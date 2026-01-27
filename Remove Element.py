class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        l = 0
        r = len(nums) - 1



        while (l <= r):
            while (l <= r and nums[r] == val):
                r -= 1
                k += 1
            while (l <= r and nums[l] != val):
                l += 1
            
            if (l > r):
                break 
                
            nums[l] = nums[r]
            nums[r] = val
            k += 1
            l += 1
            r -= 1
        
        return len(nums) - k 