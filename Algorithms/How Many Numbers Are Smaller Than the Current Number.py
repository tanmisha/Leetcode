class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums)):
            c=0
            for j in range(0,len(nums)):
                if i!=j and nums[i]> nums[j]:
                    c+=1
            ans.append(c)
        return ans