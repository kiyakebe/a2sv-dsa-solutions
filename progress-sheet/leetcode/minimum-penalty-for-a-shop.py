class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        Y = customers.count('Y') 
        N = 0

        min_penality = Y 
        min_time = 0

        print(Y, N)

        for i in range(n):
            if customers[i] == 'Y':
                Y -= 1
            else:
                N += 1

            if Y + N < min_penality:
                    min_penality = Y + N
                    min_time = i + 1

        return min_time
