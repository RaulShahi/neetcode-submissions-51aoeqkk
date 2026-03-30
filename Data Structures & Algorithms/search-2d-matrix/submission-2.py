class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])
        left = 0
        right = (m*n)-1

        while left<=right:
            mid = (left+right)//2
            r = mid//n
            c = mid%n

            print(matrix[r][c])
            if matrix[r][c] == target:
                return True
            
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False


        