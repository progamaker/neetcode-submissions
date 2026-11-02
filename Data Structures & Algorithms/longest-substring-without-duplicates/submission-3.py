class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        rep = {}
        while r<len(s):
            if s[r] not in rep:
                rep[s[r]] = r
                r+=1
                ans = max(ans, r-l)
            else:
                l=max(l, rep[s[r]] + 1)
                rep[s[r]] = r
                r+=1
                ans = max(ans,r-l)
        return ans

