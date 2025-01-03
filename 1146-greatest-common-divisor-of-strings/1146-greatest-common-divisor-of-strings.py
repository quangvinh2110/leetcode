class Solution:
    
    
    def _isCommonDivisor(self, str1: str, str2: str, divisorStr: str):
        return (divisorStr*(len(str1)//len(divisorStr))==str1) \
                and (divisorStr*(len(str2)//len(divisorStr))==str2)
    
    def _gcdOfString(self, shorter_str: str, longer_str: str) -> str:
        if shorter_str not in longer_str:
            return ""
        result = ""
        for i in range(1, len(shorter_str)+1):
            if len(shorter_str)%i==len(longer_str)%i==0:
                if self._isCommonDivisor(shorter_str, longer_str, shorter_str[:i]):
                    result = shorter_str[:i]
        return result
                    
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) >= len(str2):
            return self._gcdOfString(str2, str1)
        elif len(str1) < len(str2):
            return self._gcdOfString(str1, str2)
        
        