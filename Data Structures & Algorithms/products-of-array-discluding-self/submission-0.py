class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref= [1]*len(nums)
        pref[0] = 1
        for i in range(1,len(nums)):
            pref[i] = pref[i-1]*nums[i-1]
        suf = [1]*len(nums)
        suf[-1] = 1
        for i in range(len(nums)-1,0,-1):
            suf[i-1] = nums[i]*suf[i]
        outp = [pref[i]*suf[i] for i in range(len(nums))]
        return outp