# Day 8: Seven Segment Search
from read import read_input


digits = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

len_per_number = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

data = read_input('day_8.txt')
# part 1
output_values = []
for line in data:
    c_output_values = (line.split(' | ')[1]).split()
    output_values += c_output_values

l = list(filter(lambda x: len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7, output_values))
print(len(l))

# part 2 TO DO!!!!!!
for line in data:
    ten_possibilities = (line.split(' | ')[0]).split()




