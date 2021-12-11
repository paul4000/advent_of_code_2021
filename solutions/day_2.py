# Day 2: Dive!

from read import read_input

# part 1
commands = read_input('day_2.txt')

final_depth = 0
final_horizontal = 0

for command in commands:
    cmd_value = command.split()
    cmd = cmd_value[0]
    val = cmd_value[1]

    match cmd:
        case "forward":
            final_horizontal += int(val)
        case "down":
            final_depth += int(val)
        case "up":
            final_depth -= int(val)

print(final_depth * final_horizontal)

# part 2
final_depth = 0
final_horizontal = 0
aim = 0

for command in commands:
    cmd_value = command.split()
    cmd = cmd_value[0]
    val = cmd_value[1]
    match cmd:
        case "forward":
            final_horizontal += int(val)
            final_depth += aim * int(val)
        case "down":
            aim += int(val)
        case "up":
            aim -= int(val)

print(final_depth * final_horizontal)