class Solution:
    def minOperations(self, s: str) -> int:
        flips0 = 0
        flips1 = 0

        for i in range(len(s)):
            if (i % 2 == 0):
                if (s[i] == '0'):
                    flips1 += 1
                else:
                    flips0 += 1
            else:
                if (s[i] == '1'):
                    flips1 += 1
                else:
                    flips0 += 1
        return min(flips1, flips0)