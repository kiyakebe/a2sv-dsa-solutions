class Solution:
    def simplifyPath(self, path: str) -> str:
        path_ls = [x for x in path.split("/") if x != "" and x != "."]
        simplified_path = []

        for i in path_ls:
            if i == '..':
                if simplified_path:
                    simplified_path.pop()
            else:
                simplified_path.append(i)

        return '/' + "/".join(simplified_path)
