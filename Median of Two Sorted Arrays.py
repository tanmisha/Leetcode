class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        print(nums)
        x=len(nums)
        return  (nums[x//2]+nums[(x//2)-1])/2 if x%2==0 else nums[x//2]