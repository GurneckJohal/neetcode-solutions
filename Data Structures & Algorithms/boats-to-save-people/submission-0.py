class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0

        r = len(people) - 1

        boats = 0
        while l<=r:
            if l == r:
                l+=1
                r-=1
                boats += 1
            elif people[r] == limit:
                r-=1
                boats +=1
            elif people[r] + people[l] > limit:
                r-=1
                boats += 1
            else:
                r-=1
                l+=1
                boats+=1
        return boats