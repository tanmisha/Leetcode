class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=""
        for i in range(len(indices)):
            n+=s[indices.index(i)]
        return n