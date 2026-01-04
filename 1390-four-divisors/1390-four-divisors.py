from math import sqrt
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        totals=0
        for n in nums:
            div=set()
            lim=int(sqrt(n))
            for i in range (1, lim+1):
                if n % i==0:
                    div.add(i)
                    div.add(n//i)
                if len(div)>4:
                    break
            if len(div)==4:
                totals+=sum(div)
        return totals