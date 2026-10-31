class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = dict()
        for i,item in enumerate(nums):
            if item not in hash1:
                hash1[item] = i
        for i in range(len(nums)):
            if target - nums[i] in hash1 and i!=hash1[target - nums[i]]:
                mi = min(i,hash1[target - nums[i]])
                ma = max(i,hash1[target - nums[i]])
                return [mi,ma]