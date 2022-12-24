#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    pascal_triangle = [0] * n

    for i in range(n):
          # The first and last elements in each row are always 1
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1
        
         # Generate the values for the rest of the elements in the row
        for j in range(1, i):
            if j > 0 and j < len(row):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


    
    
           
           
