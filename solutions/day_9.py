# Day 9: Smoke Basin
from read import read_input


def compute_basin(matrix, x, y, basin):
    point = (x, y)
    val = int(matrix[x][y])
    basin.add(point)
    # check all adjusted points if they belong to basin
    left = int(matrix[x][y-1]) if y-1 >= 0 else -1
    if val < left < 9:
        basin |= compute_basin(matrix, x, y-1, basin)
    right = int(matrix[x][y+1]) if y+1 < len(matrix[x]) else -1
    if val < right < 9:
        basin |= compute_basin(matrix, x, y+1, basin)
    up = int(matrix[x-1][y]) if x-1 >= 0 else -1
    if val < up < 9:
        basin |= compute_basin(matrix, x-1, y, basin)
    bottom = int(matrix[x+1][y]) if x+1 < len(matrix) else -1
    if val < bottom < 9:
        basin |= compute_basin(matrix, x+1, y, basin)
    return basin


data = read_input('day_9.txt')
matrix = [list(row) for row in data]

no_rows = len(data)
no_columns = len(data[0])
low_points = []
basins = []
for i in range(0, no_rows):
    for j in range(0, no_columns):
        considered_point = int(matrix[i][j])
        # adjacent in same row
        left = int(matrix[i][j-1]) if j-1 >= 0 else 10
        right = int(matrix[i][j+1]) if j+1 < no_columns else 10
        # adjacent in same column
        up = int(matrix[i-1][j]) if i-1 >= 0 else 10
        bottom = int(matrix[i+1][j]) if i+1 < no_rows else 10
        if considered_point < left \
                and considered_point < right \
                and considered_point < up \
                and considered_point < bottom:
            low_points.append(considered_point)
            basin = compute_basin(matrix, i, j, set())
            basins.append(basin)

result_basins = list(reversed(sorted(basins, key=len)))
# print('Result : ' + str(sum(low_points) + len(low_points)))
print('Result : ' + str(len(result_basins[0])*len(result_basins[1])*len(result_basins[2])))

