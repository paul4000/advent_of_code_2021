# Day 3: Binary Diagnostic

from read import read_input


def get_counting_results(records_list):
    record_size = len(records_list[0]) if records_list else 0
    counting = [0] * record_size
    for record in records_list:
        for i, bit in enumerate(record):
            if bit == '1':
                counting[i] += 1
    return counting


def oxygen_condition(counting_list, bit_number, current_pivot):
    return '1' if counting_list[bit_number] >= current_pivot else '0'


def co2_condition(counting_list, bit_number, current_pivot):
    return '0' if counting_list[bit_number] >= current_pivot else '1'


def find_rating(condition, records_list, considered_bit_index):
    c_results = get_counting_results(records_list)
    r_pivot = len(records_list) / 2
    new_records_list = []
    keep_condition = condition(c_results, considered_bit_index, r_pivot)

    for ox_record in records_list:
        if ox_record[considered_bit_index] == keep_condition:
            new_records_list.append(ox_record)

    if len(records_list) == 1:
        return records_list[0]
    else:
        return find_rating(condition, new_records_list, considered_bit_index + 1)


# part 1
diag_records = read_input('day_3.txt')
records_length = len(diag_records)
counting_results = get_counting_results(diag_records)
gamma_rate = ''
epsilon_rate = ''
pivot = records_length / 2
for freq in counting_results:
    if freq > pivot:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

# print('gamma : ' + gamma_rate)
# print('epsilon : ' + epsilon_rate)
# print('dec gamma ' + str(int(gamma_rate, 2)))
# print('dec epsilon ' + str(int(epsilon_rate, 2)))
# power_consumption = int(gamma_rate, 2)*int(epsilon_rate, 2)
# print(power_consumption)

# part 2
# oxygen generator rating
oxygen_generator_rating = find_rating(oxygen_condition, diag_records, 0)
print('oxygen:' + oxygen_generator_rating)
# CO2 scrubber rating
co2_scrubber_rating = find_rating(co2_condition, diag_records, 0)
print('CO2 scrubber:' + co2_scrubber_rating)

life_support_rating = int(oxygen_generator_rating, 2)*int(co2_scrubber_rating,2)
print('general rating: ' + str(life_support_rating))


