class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        words = " " + " ".join(words)
        return words.count(" "+pref)