class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 
        merged_str = ""
        for i in range(min(len(word1), len(word2))):
            merged_str+=(word1[i] + word2[i])
        if len(word1) > len(word2):
            redundant_ind = len(word1) - len(word2)
            merged_str+=word1[-redundant_ind:]
        elif len(word2) > len(word1):
            redundant_ind = len(word2) - len(word1)
            merged_str+=word2[-redundant_ind:]
            
        return merged_str
        