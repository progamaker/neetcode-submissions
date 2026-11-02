class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        r=0
        freq_seen = dict()
        while r<len(s):
            if s[r] not in freq_seen:
                freq_seen[s[r]] = 1
            else:
                freq_seen[s[r]]+= 1
            cur_max= max(list(freq_seen.values()))
            if cur_max+k>=(r-l+1):
                ans = max(ans,r-l+1)
            else:
                freq_seen[s[l]]-=1
                l+=1
            r+=1
        return ans


