class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)

        if length % 2 == 1 or (s[0] == ')' and locked[0] == '1') or (s[-1] == '(' and locked[-1] == '1'):
            return False

        open_brackets = []
        unlocked = []

        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True