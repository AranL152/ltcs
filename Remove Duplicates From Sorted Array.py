class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        next = 1
        tracker = 0
        
        
        if (len(nums) == 1):
            return k
        
        while (tracker < len(nums) and next < len(nums)):
            orig = nums[tracker]
            while (tracker < len(nums)-1 and nums[tracker] == orig):
                tracker += 1
            nums[next] = nums[tracker]
            next += 1
            if (tracker == len(nums) - 1):
                break
        
        print(nums)

        for i in range(len(nums)-1):
            if (nums[i+1] > nums[i]):
                k += 1
            else:
                break
        return k
                
            
            
        
        
        
        
        
        
        
            
            

        