class Solution(object):
    def reverse(self, x):
        n=False
        ans=0
        if x<0:
            n=True
            x=abs(x)
        while x!=0:
            temp=x%10
            ans=ans*10+temp
            x=x//10
        if ans <- 2**31 or ans > 2**31-1:
            return 0
        return ans if n == False else -abs(ans)