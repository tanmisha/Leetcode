class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ls=""
        for i in strs:
            for j in range(len(i)):
                ls=ls.append(str[i][j])
                