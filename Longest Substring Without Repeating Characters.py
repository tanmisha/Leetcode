class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        seen={}
        l=r=0
        longest=1
        while r<len(s):
            if s[r] in seen:
                l=max(l,seen[s[r]]+1)
            longest=max(longest,r-l+1)
            seen[s[r]]=r
            r+=1
            print(l,r,longest)
        return longest
                
        
                        

            

        