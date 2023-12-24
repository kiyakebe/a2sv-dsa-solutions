class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        your_optimised_move = abs(target[0]) + abs(target[1])
        for i in ghosts:
            ghosts_move = abs(target[0] - i[0]) + abs(target[1] - i[1])
            if ghosts_move <= your_optimised_move: return False
        return True