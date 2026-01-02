class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mapp={}
        for i in nums:
            mapp[i]=mapp.get(i,0)+1
            if mapp[i]>1:
                return i