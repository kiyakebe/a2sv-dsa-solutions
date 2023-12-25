class Solution:
    def romanToInt(self, s: str) -> int:
        st = []
        sum_int = 0
        notEmpty = False
        roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        for i in s:
            val = roman_to_decimal[i]
            if notEmpty and (st[-1] < val):
                x = st.pop()
                sum_int += val-2*x # first substruct and then add the difference of val and x
                st.append(val-x)
            else:
                sum_int += val
                st.append(val)
                notEmpty = True
        return sum_int