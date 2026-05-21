class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []

        for i in range(rowIndex+1):
            row = [1] * (i+1)

            for j in range(1, i):
                row[j] = triangle[j-1] + triangle[j]
            triangle = row
        
        return triangle

        