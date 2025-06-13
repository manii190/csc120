def diag2list_rec(grid, i=0):
    if i >= len(grid):
        return []
    return [grid[i][i]] + diag2list_rec(grid, i+ 1)