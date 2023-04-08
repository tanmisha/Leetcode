class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        s,answer=sum(nums),[0]*len(nums)
        ls=0
        for i in range(0,len(nums)):
            rs=s-ls-nums[i]
            answer[i]=abs(ls-rs)
            ls+=nums[i]
        return answer