class Solution:
    def interpret(self, command: str) -> str:
        ch = ''
        ans = ""
        for i in command:
            ch += i
            if ch == "G":
                ans += ch
                ch = ''
            elif ch == "()":
                ans += 'o'
                ch = ''
            elif ch == "(al)":
                ans += "al"
                ch=''
        return  ans