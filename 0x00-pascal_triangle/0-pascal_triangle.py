#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        # The first and last elements in each row are always 1
        row = [1] * (i + 1)
        if i > 1:
            # Generate the values for the rest of the elements in the row
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
