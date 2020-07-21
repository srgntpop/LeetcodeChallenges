class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        currow = len(matrix)-1
        n = len(matrix[0])
        
        # start from the back of the aux row but dec each currow
        auxrowcol = n - 1
        
        while currow >= 0:
            # reverse values in currow
            for i in range(n//2):
                matrix[currow][i], matrix[currow][n-1-i] = matrix[currow][n-1-i], matrix[currow][i] 
            print(matrix[currow])
            # start from the first row
            auxrow = 0

            # always start from the back of the currow
            currowcol = n - 1
            
            while auxrow < currow:
                matrix[currow][currowcol], matrix[auxrow][auxrowcol] = matrix[auxrow][auxrowcol], matrix[currow][currowcol] 
                auxrow += 1
                currowcol -= 1
            print(matrix[currow])
            currow -= 1
            auxrowcol -= 1
            
        return
        
        
        
