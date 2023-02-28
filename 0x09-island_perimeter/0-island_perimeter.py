#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # check right
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check bottom
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
    return perimeter
