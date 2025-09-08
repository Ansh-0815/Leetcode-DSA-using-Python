class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m =len(haystack),len(needle)
        l=0 
        while l<=n-m:
            if haystack[l:l+m]==needle:
                return l
            l+=1
        return -1