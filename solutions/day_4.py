# Day 4: Giant Squid

from read import read_input
import itertools


class Board:

    def __init__(self, board_array):
        self.internal_board = [[number for number in board_row.split()] for board_row in board_array]
        self.marked_numbers_indices = []
        self.board_size = 5

    def __str__(self):
        return str(self.internal_board)

    def mark_number(self, number_to_find):
        found_indices = [(y, x) for x, row in enumerate(self.internal_board) for y, column_numb in enumerate(row)
                         if column_numb == number_to_find]
        self.marked_numbers_indices += found_indices
        return found_indices

    def is_winner(self):
        x_list = [x for x, y in self.marked_numbers_indices]
        x_duplicates = Board._duplicates(x_list)
        x_full = [1 for dup_row in x_duplicates if len(dup_row) == self.board_size]
        y_list = [y for x, y in self.marked_numbers_indices]
        y_duplicates = Board._duplicates(y_list)
        y_full = [1 for dup_row in y_duplicates if len(dup_row) == self.board_size]
        return x_full or y_full

    def sum_of_unmarked(self):
        return sum([int(column_numb) for x, row in enumerate(self.internal_board) for y, column_numb in enumerate(row)
                            if (y, x) not in self.marked_numbers_indices])

    @staticmethod
    def _duplicates(lis):
        return [list(li) for i, li in itertools.groupby(sorted(lis))]


# part 1 & 2
board_lines = read_input('day_4_boards.txt')
boards_without_pause = list(filter(lambda line: line, board_lines))
board_size = 5
boards_raw = [boards_without_pause[i:i + board_size] for i in range(0, len(boards_without_pause), board_size)]
boards = [Board(raw) for raw in boards_raw]

randoms = read_input('day_4_sequence.txt')[0].split(',')
for ran in randoms:
    for board in boards:
        if not board.is_winner():
            board.mark_number(ran)
            if board.is_winner():
                final_score = board.sum_of_unmarked()*int(ran)
                print(str(final_score) + ' last number ' + str(ran))

