class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        temp=x
        rev=0
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        return rev==temp
