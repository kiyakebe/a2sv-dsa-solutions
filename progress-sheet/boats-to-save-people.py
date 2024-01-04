class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat_counter = 0
        while left <= right:
            if(people[right] + people[left] <= limit):
                left += 1
                right -= 1
            else:
                right -= 1
            boat_counter += 1

        return boat_counter