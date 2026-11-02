class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r= len(s1)
        ans = dict()
        cur = dict()
        for i in s1:
            if i not in ans:
                ans[i]=1
            else:
                ans[i]+=1
        for i in s2[:len(s1)]:
            if i not in cur:
                cur[i]=1
            else:
                cur[i]+=1
        
        while r<len(s2):
            if cur==ans:
                return True
            cur[s2[l]]-=1
            if s2[r] not in cur:
                cur[s2[r]]=1
            else:
                cur[s2[r]]+=1
            if cur[s2[l]]==0:
                del cur[s2[l]]
            r+=1
            l+=1
        
        return cur==ans