class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if('()' in s or '{}' in s or '[]' in s):
                s=s.replace('()','').replace('{}','').replace('[]','')
        return True if len(s)==0 else False