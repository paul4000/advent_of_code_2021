# # Day 10: Syntax Scoring
from math import floor

from read import read_input
from functools import reduce

matching_for_closing = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '['
}

points_for_invalids = {
    ')': 3,
    '}': 1197,
    '>': 25137,
    ']': 57
}

matching_for_opening = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']'
}

points_for_valids = {
    ')': 1,
    '}': 3,
    '>': 4,
    ']': 2
}


def get_invalid_character_if_any(line):
    left_brackets_stack = list()
    for char in line:
        if matching_for_closing.get(char):
            if left_brackets_stack and left_brackets_stack[-1] == matching_for_closing.get(char):
                left_brackets_stack.pop()
            else:
                return char
        else:
            left_brackets_stack.append(char)
    return None


def find_autocompleted_part(line):
    if get_invalid_character_if_any(line):
        return []
    left_brackets_stack = list()
    for char in line:
        if matching_for_closing.get(char):
            if left_brackets_stack and left_brackets_stack[-1] == matching_for_closing.get(char):
                left_brackets_stack.pop()
        else:
            left_brackets_stack.append(char)
    return [matching_for_opening.get(opening) for opening in reversed(left_brackets_stack)]


data = read_input('day_10.txt')
invalid_chars = []

# part 1
for line in data:
    invalid_character = get_invalid_character_if_any(line)
    if invalid_character:
        invalid_chars.append(invalid_character)

points_for_inv_chars = list(map(lambda x: points_for_invalids.get(x), invalid_chars))
# print('Result : ' + str(sum(points_for_inv_chars)))

# part 2
autocompleted_parts = []
for line in data:
    autocompleted_part = find_autocompleted_part(line)
    if autocompleted_part:
        autocompleted_parts.append(autocompleted_part)

autocompleted_scores = []
for ap in autocompleted_parts:
    p_ap = list(map(lambda x: points_for_valids.get(x), ap))
    score = reduce(lambda acc, x: acc * 5 + x, p_ap, 0)
    autocompleted_scores.append(score)

middle_index = floor(len(autocompleted_scores)/2)
print(str(sorted(autocompleted_scores)[middle_index]))

