class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = dict()
        for i,item in enumerate(nums):
            if (target - item) in hash1:
                return [hash1[target - item],i]
            hash1[item] = i
        