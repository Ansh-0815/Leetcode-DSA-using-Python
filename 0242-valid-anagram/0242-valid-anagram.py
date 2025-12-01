class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        for j in t:
            if j not in hash:
                return False
            hash[j]-=1
            if hash[j]<0:
                return False
        return True