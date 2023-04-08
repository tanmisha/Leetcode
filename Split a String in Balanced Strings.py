class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=r=c=0
        for i in s:
            if i=='R':
                r+=1
            else:
                l+=1
            if l==r:
                c+=1
        return c
            