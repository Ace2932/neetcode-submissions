class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroColumns = []
        zeroRows = []

        for rowIndex, row in enumerate(matrix):
            for colIndex, number in enumerate(row):
                if(number == 0):
                    zeroColumns.append(colIndex)
                    zeroRows.append(rowIndex)
        for i in range(len(matrix[0])):
            for number in zeroRows:
                matrix[number][i] = 0

        for row in matrix:
            for number in zeroColumns:

                row[number] = 0

    
