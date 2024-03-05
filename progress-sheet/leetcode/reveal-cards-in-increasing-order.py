class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque([deck.pop()])

        for i in reversed(deck):
            dq.appendleft(dq.pop())
            dq.appendleft(i)
        return dq