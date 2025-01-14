class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        num_set = set()
        result = []
        for ind, (num_a, num_b) in enumerate(zip(A, B)):
            num_set.update([num_a, num_b])
            result.append((ind+1)*2-len(num_set))
        return result
        