class ATM:

    def __init__(self):
        # crate a dictionary for [500, 200, 100, 50, 20] note count
        self.notes = [20, 50, 100, 200, 500]
        self.atm_balance = [0 for _ in range(5)]

    def deposit(self, banknotesCount: List[int]) -> None:
       for i in range(5):
           self.atm_balance[i] += banknotesCount[i] 

    def withdraw(self, amount: int) -> List[int]:
        withdraw_notes = [0 for _ in range(5)]

        for i in range(4, -1, -1):
            curr_note_count = amount//self.notes[i]
            amount %= self.notes[i]

            if curr_note_count == 0:
                continue
            elif self.atm_balance[i] == 0:
                amount +=  self.notes[i]*curr_note_count
            elif self.atm_balance[i]:
                if curr_note_count <= self.atm_balance[i]:
                    self.atm_balance[i] -= curr_note_count
                    withdraw_notes[i] = curr_note_count
                else:
                    amount += (curr_note_count - self.atm_balance[i]) * self.notes[i]
                    withdraw_notes[i] = self.atm_balance[i]
                    self.atm_balance[i] = 0
            
        if amount != 0:
            for i in range(5):
                self.atm_balance[i] += withdraw_notes[i]
            return [-1]

        return withdraw_notes


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)