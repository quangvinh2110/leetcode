class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        waterHeight = [[0 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]
        height=1
        index_stack = [[]]
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]==1:
                    index_stack[0].append((i, j))
        # print(index_stack)
        while index_stack[0]:
            index_stack.append([])
            for i, j in index_stack[0]:
                if i<len(isWater)-1 and isWater[i+1][j]==0:
                    isWater[i+1][j]=1
                    waterHeight[i+1][j]=height
                    index_stack[1].append((i+1, j))
                if j<len(isWater[0])-1 and isWater[i][j+1]==0:
                    isWater[i][j+1]=1
                    waterHeight[i][j+1]=height
                    index_stack[1].append((i, j+1))
                if i>0 and isWater[i-1][j]==0:
                    isWater[i-1][j]=1
                    waterHeight[i-1][j]=height
                    index_stack[1].append((i-1, j))
                if j>0 and isWater[i][j-1]==0:
                    isWater[i][j-1]=1
                    waterHeight[i][j-1]=height
                    index_stack[1].append((i, j-1))
            del index_stack[0]
            height+=1

        return waterHeight
        


                