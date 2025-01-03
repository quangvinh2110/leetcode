class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        left = 0 
        _iter = left
        right = arr[left]
        n_splits = 1
        while right<len(arr)-1:
            while _iter <= right:
                if arr[_iter] > right:
                    right = arr[_iter]
                _iter+=1
            if right<len(arr)-1:
                n_splits+=1
                left = right+1
            else:
                break
            if left<len(arr)-1:
                right = arr[left]
                _iter = left
            else:
                break
        return n_splits