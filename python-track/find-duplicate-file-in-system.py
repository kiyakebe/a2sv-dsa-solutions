class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths_list = [path.split() for path in paths]
        d = {}
        for i in paths_list:
            for j in range(1, len(i)):

                if i[j].split('(')[1] not in d:
                    d[i[j].split('(')[1]] = []
                d[i[j].split('(')[1]].append(i[0]+'/'+i[j].split('(')[0])

        ans = [path for path in d.values() if len(path) >= 2]

        return ans