class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ret = []
        n, m = len(nums1), len(nums2)
        list1 = {}
        list2 = {}

        for i in range(n):
            if (nums1[i] not in list1):
                list1[nums1[i]] = i
        
        for i, num in enumerate(nums2):
            if num in list1 and num not in list2:
                ret.append(num)
                list2[num] = i

        return ret