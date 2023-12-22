class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            n = digits[i]
            if(n + carry > 9):
                digits[i] = (n + carry)%10
            else:
                digits[i] = n + carry

            carry = (n + carry)//10
        print(carry)
        if(carry != 0): digits.insert(0, carry)

        return digits
