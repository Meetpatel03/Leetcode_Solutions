class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = len(word1) + len(word2)
        ans = ""
        for i in range(length):
            if i< len(word1):
                ans+=word1[i]
            if i< len(word2):
                ans+=word2[i]
        return ans
