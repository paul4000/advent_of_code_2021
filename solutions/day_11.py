# Day 11: Dumbo Octopus

from read import read_input

STEPS_N = 500
SIZE_ROW = 10
SIZE_COLUMN = 10


def was_simultaneous_flash(octopuses):
    for i in range(1, SIZE_ROW + 1):
        for j in range(1, SIZE_COLUMN + 1):
            if octopuses[i][j] != 0:
                return False
    return True


data = read_input("day_11.txt")
octopuses_raw = [list(d) for d in data]
octopuses_int = [[int(x) for x in oct_r] for oct_r in octopuses_raw]
# make padding of 0
octopuses = [[0] * (SIZE_COLUMN + 2)]
for o_int_row in octopuses_int:
    new_row = [0] + o_int_row + [0]
    octopuses.append(new_row)
octopuses.append([0] * (SIZE_COLUMN + 2))

# part 1
flash_count = 0
for k in range(1, STEPS_N + 1):
    # increment octopuses
    octopuses = [[x + 1 for x in oct_r] for oct_r in octopuses]
    # flash octopuses
    was_flash = True
    while was_flash:
        was_flash = False
        for i in range(1, SIZE_ROW + 1):
            for j in range(1, SIZE_COLUMN + 1):
                if octopuses[i][j] > 9:
                    was_flash = True
                    octopuses[i][j] = -1000  # used all energy
                    flash_count += 1
                    # strengthen adjacent octopuses
                    octopuses[i - 1][j - 1] += 1
                    octopuses[i - 1][j] += 1
                    octopuses[i - 1][j + 1] += 1
                    octopuses[i][j - 1] += 1
                    octopuses[i][j + 1] += 1
                    octopuses[i + 1][j - 1] += 1
                    octopuses[i + 1][j] += 1
                    octopuses[i + 1][j + 1] += 1
    # transform minuses into 0
    for i in range(1, SIZE_ROW + 1):
        for j in range(1, SIZE_COLUMN + 1):
            if octopuses[i][j] < 0:
                octopuses[i][j] = 0
    # part 2 - find first simultaneous flash
    if was_simultaneous_flash(octopuses):
        print("step " + str(k))

print("Flesh count " + str(flash_count))
