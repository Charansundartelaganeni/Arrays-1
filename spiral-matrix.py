#TC: O(m*n)
#SC: O(m*n)



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        result = []
        
        while left<=right and top<=bottom: #loop until left doesn't cross right and top and bottom doesn't collide
            for i in range(left,right+1): #traversing from left to right
                result.append(matrix[top][i]) #append the top row values to result
            top+=1
            
            for k in range(top,bottom+1): #traversing from top to bottom
                result.append(matrix[k][right]) #append the right column values to result
            right-=1
            
            if top<=bottom:  #if top is less than bottom
                for m in range(right,left-1,-1): #traverse from right to left
                    result.append(matrix[bottom][m]) #append the bottom row elements to result
            bottom-=1
            
            if left<=right: #if left is less than right
                for n in range(bottom,top-1,-1): #traverse from bottom to top
                    result.append(matrix[n][left]) #append the left column values to result
            left+=1
        
        return result