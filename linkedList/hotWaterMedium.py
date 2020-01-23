'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answerList = []
        mainList = []
        for mainLine in range(height):
            for testLine in range(height):
                if testLine == mainList:
                    answerList[testLine] = 0
                    continue
                elif height[testLine] < height[mainLine]:
                    answerList[testLine] = 0
                else:
                    area = height[mainLine] * abs(testLine - mainList)
                    answerList[testLine] = area
            mainList = max(answerList)
        return max(mainList)
'''
h = [1,2,1,4,5]

for i in h:
	print(i)