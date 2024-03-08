class Solution:
    def __init__(self):
        self.n = 0
        self.ans = []

    def find_sum(self, indices):
        lng = len(indices)
        pref = [0]*lng

        pref[0] = indices[0]
        for i in range(1,lng):
            pref[i] = pref[i-1] + indices[i]

        for i in range(lng):
            if i == 0:
                self.ans[indices[i]] = pref[-1] - lng*indices[i]
            elif i == lng-1:
                self.ans[indices[i]] = lng*indices[i] - pref[-1]
            else:
                # left_side + right_side
                right_side = (pref[-1] - pref[i]) - indices[i]*(lng-(i+1))
                left_side = indices[i]*i - pref[i-1]
                self.ans[indices[i]] = right_side + left_side
        return

    def distance(self, nums: List[int]) -> List[int]:
        index_list = defaultdict(list)
        self.n = len(nums)
        self.ans = [0]*self.n

        for i in range(len(nums)):
            index_list[nums[i]].append(i)

        for k, v in index_list.items():
            self.find_sum(v)

        return self.ans