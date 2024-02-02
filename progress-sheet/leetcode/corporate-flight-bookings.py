class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # give it a right margin to do my -1 w/o having to worry about index out of range
        ps = [0 for i in range(n+1)]

        for f, l, s in bookings:
            ps[f-1] += s
            ps[l] -= s
        for i in range(1, n+1):
            ps[i] += ps[i-1]
        ps.pop()
        return(ps)
