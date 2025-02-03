# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1 = len(str1)
        len_2 = len(str2)

        len_gcd = gcd(len_1, len_2)

        posible_sgcd = str1[:len_gcd]

        if posible_sgcd*(len_1//len_gcd) == str1 and posible_sgcd*(len_2//len_gcd) == str2:
            return posible_sgcd
        
        return ''