class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        numBoats = 0

        while (l <= r):

            numBoats += 1

            if people[l] + people[r] <= limit:
                l += 1
            r -= 1

        return numBoats
