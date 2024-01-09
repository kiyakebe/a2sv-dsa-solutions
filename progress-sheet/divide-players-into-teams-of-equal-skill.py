class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1

        chemistry_sum = 0
        val = skill[0] + skill[-1]
        while left < right:
            if skill[left] + skill[right] == val:
                chemistry_sum += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return chemistry_sum
