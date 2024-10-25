# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for i in range(1, len(folder)):
            if folder[i] == ans[-1] or folder[i].startswith(ans[-1]+'/'):
                continue
            ans.append(folder[i])
        
        return ans