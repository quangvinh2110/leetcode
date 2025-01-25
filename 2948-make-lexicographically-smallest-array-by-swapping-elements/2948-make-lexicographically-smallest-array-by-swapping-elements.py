class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x:x[1])
        clusters = [[sorted_nums[0]]]
        for ind, val in sorted_nums[1:]:
            if val-clusters[-1][-1][1]<=limit:
                clusters[-1].append((ind, val))
            else:
                clusters.append([(ind, val)])
        clusters = list(map(lambda l: list(zip(*l)), clusters))
        clusters = list(map(lambda e: (sorted(e[0]), e[1]), clusters))
        result = [0 for _ in range(len(nums))]
        for cluster in clusters:
            for ind, val in zip(*cluster):
                result[ind] = val
        return result