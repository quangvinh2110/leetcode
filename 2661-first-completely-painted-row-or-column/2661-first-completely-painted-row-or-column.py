class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hashmap = {arr[i]: i for i in range(len(arr))}
        new_mat = [[hashmap[c] for c in row] for row in mat]
        transposed_new_mat = list(zip(*new_mat))
        return min(map(max, new_mat+transposed_new_mat))
        