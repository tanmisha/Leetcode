class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev = 0
        for i in digits:
            rev = (rev * 10) + i
        rev += 1
        res = [int(x) for x in str(rev)]
        return res