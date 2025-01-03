class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        for e in arr:
            if e==0 and counter[0]>1:
                return True
            if e!=0 and e*2 in counter:
                return True
        return False
        