#TC: O(m*n)
#SC: O(m*n)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = [0] * (rows * cols) #result is initialized with zeroes

        index=0
        r=0
        c=0 
        dir_=1 #initially direction is set to one
        
        while(index<len(result)):
            result[index] = mat[r][c] 
            #up
            if dir_ == 1:   #if direction is one, we should move up
                if c == cols -1: #if it is the last column, increase the row and change the direction
                    r+=1
                    dir_=-1
                elif r==0: #if it is the first row, increse the column and change the direction
                    c+=1
                    dir_=-1
                else: #else increase the column and decrease the row
                    r-=1
                    c+=1
            #down
            elif dir_ == -1:
                if r == rows-1: #if it is the first row, increase the column and change the direction
                    c+=1
                    dir_=1
                elif c==0:#if it is the first column, increse the row and change the direction
                    r+=1
                    dir_=1
                else: #else increase the row and decrease the column
                    r+=1
                    c-=1
            index+=1
        return result