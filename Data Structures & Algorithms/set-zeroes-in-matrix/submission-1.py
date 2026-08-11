class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroColumns = []
        zeroRows = []

        for rowIndex, row in enumerate(matrix):
            for colIndex, number in enumerate(row):
                if(number == 0):
                    zeroColumns.append(colIndex)
                    zeroRows.append(rowIndex)
        
        for rowIndex, row in enumerate(matrix):
            for colIndex, number in enumerate(row):
                if (colIndex in zeroColumns) or (rowIndex in zeroRows):
                    matrix[rowIndex][colIndex] = 0
                

    
