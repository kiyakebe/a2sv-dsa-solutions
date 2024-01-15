class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = defaultdict(int)
        _min = float("inf")
        card_exists = False
        for i in range(len(cards)):
            if cards[i] in d:
                _min = min(_min ,i-d[cards[i]]+1)
                card_exists = True
            d[cards[i]] = i
        if not card_exists:
            return -1
        return _min