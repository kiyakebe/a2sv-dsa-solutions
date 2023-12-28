class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        front = set(fronts)
        back = set(backs)

        goods = front | back

        for i in range(n):
            if fronts[i] == backs[i]:
                goods.discard(fronts[i])

        if goods: return min(goods)
        return 0

