class Solution:
    def maxScore(self, s: str) -> int:
        score_left = 0
        max_score_left = -1
        num_1s = 0
        for c in s[:-1]:
            if c=="0":
                score_left+=1
                if max_score_left < score_left:
                    max_score_left = score_left
            if c=="1":
                score_left-=1
                num_1s+=1
        if s[-1]=="1":
            num_1s+=1
        return max_score_left+num_1s
        