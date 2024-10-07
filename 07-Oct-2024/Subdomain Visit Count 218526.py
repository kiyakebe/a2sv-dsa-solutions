# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        ans = []
        for i in cpdomains:
            val, domain = i.split()
            val = int(val)
            subdomain = domain.split('.')

            for i in range(len(subdomain)):
                key = '.'.join(subdomain[i:len(subdomain)])
                d[key] = d.get(key, 0) + val
        for key, val in d.items():
            ans.append(str(val)+ " " + key)
        
        return ans