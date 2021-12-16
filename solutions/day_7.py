# Day 7: The Treachery of Whales
from read import read_input

data = read_input('day_7.txt')
crab_positions = [int(d) for d in data[0].split(',')]
possible_fuel_usage = []
first_crab = min(crab_positions)
last_crab = max(crab_positions)


def get_fuel_usage(dest_position, crab):
    return sum(list(range(1, abs(dest_position - crab)+1)))


# compute every option from one to last crab
for possible_position in range(first_crab, last_crab+1):
    fuel_usage_of_all_crabs = sum([get_fuel_usage(possible_position, crab) for crab in crab_positions])
    possible_fuel_usage.append(fuel_usage_of_all_crabs)

print("Minimum fuel usage : " + str(min(possible_fuel_usage)))