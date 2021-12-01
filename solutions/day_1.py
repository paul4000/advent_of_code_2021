# Day 1: Sonar Sweep

from read import read_input
from more_itertools import triplewise
import itertools as it

# part 1
measurements = read_input('day_1.txt')
how_many_increased = 1  # first measurement counted as increased
for first, second in it.pairwise(measurements):
    if first < second:
        how_many_increased += 1
print(how_many_increased)

# part 2

measurement_sums = []
for first, second, third in triplewise(measurements):
    m_sum = int(first) + int(second) + int(third)
    measurement_sums.append(m_sum)
how_many_increased = 0
for first, second in it.pairwise(measurement_sums):
    if first < second:
        how_many_increased += 1
print(how_many_increased)

