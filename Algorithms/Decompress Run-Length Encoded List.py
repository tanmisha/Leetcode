class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        while(i<len(nums)):
            j=1
            while(j<=nums[i]):
                ans.append(nums[i+1])
                j+=1
            i+=2
        return ans    