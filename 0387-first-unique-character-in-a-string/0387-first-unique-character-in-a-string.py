class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        for j in range (len(s)):
            if hash[s[j]]==1:
                return j
        return -1
