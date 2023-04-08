class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new,j=[0]*2*n,0
        for i in range(n):
            new[j]=nums[i]
            new[j+1]=nums[n+i]
            j+=2
        return new