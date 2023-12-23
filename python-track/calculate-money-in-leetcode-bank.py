class Solution:
    def totalMoney(self, n: int) -> int:
        week=n//7
        day=n%7
        total=0
        for i in range(week):
            if i==0: total += (i+7)*(i+8)//2;
            else: total += (i+7)*(i+8)//2 - i*(i+1)//2;

        if week==0: total += (day+week)*(day+week+1)//2;
        else: total += (day+week)*(day+week+1)//2 - (week)*(week+1)//2; 
        return total