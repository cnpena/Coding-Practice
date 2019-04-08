# 118. Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution(object):
    # Compute each row using the values from the previous row
    def generate(self, numRows):
        output = []
        
        for rowNum in range(numRows):
            row = [1] # Row begins with a 1
            
            for i in range(1, rowNum): # Append rest of values to row
                left = output[rowNum-1][i-1]
                right = output[rowNum-1][i]
                row.append(left + right)
                
            if rowNum > 0: # Row ends with a 1
                row.append(1)
                
            output.append(row)
        return output