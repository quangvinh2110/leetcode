class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin1, bin2 = f'{num1:b}', f'{num2:b}'
        num_1s_1 = bin1.count("1")
        num_1s_2 = bin2.count("1")
        if num_1s_1==num_1s_2:
            return num1

        x = list(bin1)
        if num_1s_1>num_1s_2:
            for ind, char in enumerate(x):
                if char=="1":
                    if num_1s_2>0:
                        num_1s_2-=1
                    else:
                        x[ind]="0"
        else:
            ind = len(x)-1
            count = num_1s_2-num_1s_1
            while ind>-1 and count>0:
                if x[ind]=="0":
                    x[ind]="1"
                    count-=1
                ind-=1
            if count>0:
                x = ["1"]*count + x
        return int("".join(x), 2)