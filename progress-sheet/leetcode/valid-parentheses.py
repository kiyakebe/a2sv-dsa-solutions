class Solution:
    def isValid(self, s: str) -> bool:
        valid_par = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        n = len(s)
        p_stack = []
        for i in range(n):
            if s[i] in valid_par.values():
                p_stack.append(s[i])
            elif not p_stack or p_stack.pop() != valid_par[s[i]]:
                    return False

        if not p_stack:
            return True
        return False