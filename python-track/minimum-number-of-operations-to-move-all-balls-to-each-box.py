class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        box_with_ball = [i for i in range(n) if boxes[i] == '1']

        for i in range(n):
            sum_moves = sum([abs(j - i) for j in box_with_ball])
            ans.append(sum_moves)
        return ans