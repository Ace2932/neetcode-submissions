class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        width = len(matrix[0])
        depth = len(matrix)
        top = 0
        right = width
        bottom = depth - 1
        left = 0

        rowPosition = 0
        depthPosition = 0

        
        spiral = []
        while len(spiral) < (width * depth):
            spiral += self.grabRight(matrix, top, left, right)
            top += 1
            spiral += self.grabDown(matrix, top, bottom, right)
            right -= 1
            if top <= bottom:
                spiral += self.grabLeft(matrix, bottom, left, right)
                bottom -= 1
            if left < right:
                spiral += self.grabUp(matrix, top, bottom, left)
                left += 1
            
        return spiral

    
    def grabRight(self, matrix: List[List[int]], top, left, right) -> List[int]:
        return matrix[top][left:right]
    def grabDown(self, matrix: List[List[int]], top, bottom, right) -> List[int]:
        col = right - 1
        return [matrix[r][col] for r in range(top, bottom + 1)]

    def grabLeft(self, matrix: List[List[int]], bottom, left, right) -> List[int]:
        return matrix[bottom][left:right][::-1]
    
    def grabUp(self, matrix: List[List[int]], top: int, bottom: int, left) -> List[int]: 
        return [matrix[r][left] for r in range(bottom, top - 1, -1)]


    
    
            



