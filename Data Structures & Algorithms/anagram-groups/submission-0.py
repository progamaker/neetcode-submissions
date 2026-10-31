class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for item in strs:
            item_s = ''.join(sorted(item))
            if item_s not in d:
                d[item_s] = [item]
            else:
                d[item_s].append(item)
        return list(d.values())