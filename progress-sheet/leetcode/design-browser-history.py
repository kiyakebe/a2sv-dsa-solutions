class Node:
    def __init__(self, val="", back=None, forward=None):
        self.val = val
        self.back = back
        self.forward = forward

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url, self.curr)
        self.curr.forward = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.back != None:
            self.curr = self.curr.back
            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.forward != None:
            self.curr = self.curr.forward
            steps -= 1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)