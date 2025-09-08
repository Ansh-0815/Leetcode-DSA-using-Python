class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def haszero(x):
            return '0' in str(x)
        for a in range(1,n):
            b=n-a
            if not haszero(a) and not haszero(b):
                return a,b
