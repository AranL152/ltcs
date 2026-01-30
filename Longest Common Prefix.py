class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        minlen = 201
        mindex = 0

        for i, string in enumerate(strs):
            if (minlen > len(string)):
                minlen = len(string)
                mindex = i
        
        
        
        for j, c in enumerate(strs[mindex]):
            for word in strs:
                if (c not in word[j]):
                    print(word[j])
                    return ret 

            ret = ret + c
        
        return ret







            

