class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for i in range (0,len(nums)):
            hash[nums[i]]=hash.get(nums[i],0)+1
        for j in range(len(nums)):
            if hash[nums[j]]>=2:
                return True
        return False