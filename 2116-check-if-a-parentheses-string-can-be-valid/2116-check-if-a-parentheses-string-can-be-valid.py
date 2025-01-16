class Solution:
    @classmethod
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        if s[0]==")" and locked[0]=="1":
            return False

        stack = []
        stack_ind = []
        unlocked_left = []
        unlocked_right = []

        for ind, (char, flag) in enumerate(zip(s, locked)):
            if flag=="0":
                if char==")":
                    unlocked_right.append(char)
                
            if len(stack)>0 and stack[-1]=="(" and char==")":
                stack.pop()
                stack_ind.pop()
            elif len(stack)==0 and char==")":
                if len(unlocked_right)>0:
                    stack.append("(")
                    stack_ind.append(ind)
                    unlocked_right.pop()
                else:
                    print("hfhlsjfhsl")
                    print(unlocked_right)
                    return False
            else:
                stack.append(char)
                stack_ind.append(ind)

        if not stack:
            return True

        for ind, (char, flag) in reversed(list(enumerate(zip(s, locked)))):
            if flag=="0":
                if char=="(":
                    unlocked_left.append(char)
            if len(stack_ind)==0:
                return True
            if ind==stack_ind[-1]:
                if len(unlocked_left)>0:
                    stack.pop()
                    stack.pop()
                    stack_ind.pop()
                    stack_ind.pop()
                    unlocked_left.pop()
                else:
                    return False

        # print(stack)
        # print(stack_ind)
        if not stack:
            return True
        return False
