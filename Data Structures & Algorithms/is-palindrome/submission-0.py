class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = []
        for i in s:
            if i.isalnum():
                new_s.append(i)
        new_s = ''.join(new_s)
        l = 0
        r = len(new_s)-1
        while l<r:
            if new_s[l]==new_s[r]:
                l+=1
                r-=1
            else:
                return False
        return True