class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp={}
        n=len(nums)
        for i in nums:
            mapp[i]=mapp.get(i,0)+1
            if mapp[i]>n//2:
                return i