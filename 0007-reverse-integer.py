class Solution(object):
    def reverse(self, x):
        intmax=2**31 - 1
        intmin=-2**31
        sign=-1 if x<0 else 1
        x=abs(x)
        rev=0
        while x>0:
            d=x%10
            
            x=x//10
            if rev>intmax//10 or (rev == intmax and d>7):
                return 0
            rev=rev*10+d
        return rev*sign
