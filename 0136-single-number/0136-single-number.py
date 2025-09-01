class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map={}
        n=len(nums)
        for i in range(0,n):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for k,v in hash_map.items():
            if v==1:
                return k