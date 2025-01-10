class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        results = []
        words2_counter = Counter()
        for word2 in words2:
            counter2 = Counter(word2)
            words2_counter = words2_counter | counter2
        for word1 in words1:
            counter1 = Counter(word1)
            flag = True
            for k, v in words2_counter.items():
                if counter1[k] < v:
                    flag = False
                    break
            if flag:
                results.append(word1)
        return results