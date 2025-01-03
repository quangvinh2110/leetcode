class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        count = 0
        for char in t:
            if char==s[count]:
                count+=1
            if count==len(s):
                return True
        return False
        