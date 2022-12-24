#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)

    return triangle
