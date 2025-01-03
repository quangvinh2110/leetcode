class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        return counter1.keys()==counter2.keys() and sorted(counter1.values())==sorted(counter2.values())