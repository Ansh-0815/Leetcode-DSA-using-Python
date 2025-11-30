class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        res=0
        while num>0:
            d=num%10
            res+=d
            num=num//10
        return self.addDigits(res)
