# Day 5: Hydrothermal Venture

from read import read_input


class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.x_1 = x1
        self.y_1 = y1
        self.x_2 = x2
        self.y_2 = y2

    def vertical_or_horizontal(self):
        return self.x_1 == self.x_2 or self.y_1 == self.y_2

    def vent_line_coordinates(self):
        if self.x_1 == self.x_2:
            if self.y_1 < self.y_2:
                return [(self.x_1, y) for y in range(self.y_1, self.y_2 + 1)]
            else:
                return [(self.x_1, y) for y in range(self.y_2, self.y_1 + 1)]
        if self.y_1 == self.y_2:
            if self.x_1 < self.x_2:
                return [(x, self.y_1) for x in range(self.x_1, self.x_2 + 1)]
            else:
                return [(x, self.y_1) for x in range(self.x_2, self.x_1 + 1)]
        # diagonal
        x_range = range(min(self.x_1, self.x_2), max(self.x_1, self.x_2) + 1)
        y_range = range(min(self.y_1, self.y_2), max(self.y_1, self.y_2) + 1)
        if self.x_1 < self.x_2:
            if self.y_1 < self.y_2:
                return list(zip(x_range, y_range))
            else:
                return list(zip(x_range, reversed(y_range)))
        else:
            if self.y_1 < self.y_2:
                return list(zip(reversed(x_range), y_range))
            else:
                return list(zip(reversed(x_range), reversed(y_range)))


input_data = read_input('day_5.txt')
vents = []
for row_raw in input_data:
    row = row_raw.split(',')
    vents.append(Vent(int(row[0]), int(row[1]), int(row[2]), int(row[3])))

# h_v_vents = [v for v in vents if v.vertical_or_horizontal()]

# find the biggest coordinate
v_max_x = 0
v_max_y = 0
for v in vents:
    temp_max_x = max(v.x_1, v.x_2)
    if temp_max_x > v_max_x:
        v_max_x = temp_max_x
    temp_max_y = max(v.y_1, v.y_2)
    if temp_max_y > v_max_y:
        v_max_y = temp_max_y

# initialize board for counting
board = [[0] * (v_max_x + 1) for i in range(0, v_max_y + 1)]

for vent in vents:
    coordinates = vent.vent_line_coordinates()
    for co in coordinates:
        board[co[1]][co[0]] += 1

# calculate points 2x crossed by vent
sum_of_crossed_points = 0
for row in board:
    sum_of_crossed_points += len([x for x in row if x >= 2])
print(sum_of_crossed_points)
