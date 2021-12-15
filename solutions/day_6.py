# Day 6: Lanternfish

from read import read_input

fish_data = read_input('day_6.txt')
fish_counters = [int(fish) for fish in fish_data[0].split(',')]

DAYS = 256

# 8 is max counter value which fish can have so the mapping will be:
# number of days until new fish -> no of such fishes
six_days_to_birth = 6
# [ind] -> value
how_many_fishes_per_days = [0]*9
# init state
for fish in fish_counters:
    how_many_fishes_per_days[fish] += 1

for day in range(0, DAYS):
    no_of_productive_fishes = how_many_fishes_per_days[0]
    # rotate in left
    how_many_fishes_per_days = how_many_fishes_per_days[1:] + how_many_fishes_per_days[:1]
    how_many_fishes_per_days[six_days_to_birth] += no_of_productive_fishes

print('No of fishes Lanternfishes after '+ str(DAYS) +' days: ' + str(sum(how_many_fishes_per_days)))
