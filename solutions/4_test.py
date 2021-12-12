import unittest
from day_4 import Board


class TestBoard(unittest.TestCase):
    def test_is_winner(self):
        # check x
        b = Board(['24 75 59 41 17',
                   '58 74 64 92 39',
                   '68  8 78 85 72',
                   '18  3 22  4 34',
                   '11 76  6 28 50'])
        b.mark_number('18')
        b.mark_number('4')
        self.assertFalse(b.is_winner())
        b.mark_number('28')
        self.assertFalse(b.is_winner())
        b.mark_number('3')
        self.assertFalse(b.is_winner())
        b.mark_number('22')
        self.assertFalse(b.is_winner())
        b.mark_number('34')
        self.assertTrue(b.is_winner())
        # check y
        b2 = Board(['24 75 59 41 17',
                    '58 74 64 92 39',
                    '68  8 78 85 72',
                    '18  3 22  4 34',
                    '11 76  6 28 50'])
        b2.mark_number('75')
        b2.mark_number('24')
        b2.mark_number('59')
        self.assertFalse(b2.is_winner())
        b2.mark_number('76')
        b2.mark_number('8')
        self.assertFalse(b2.is_winner())
        b2.mark_number('28')
        b2.mark_number('50')
        self.assertFalse(b2.is_winner())
        b2.mark_number('74')
        b2.mark_number('3')
        self.assertTrue(b2.is_winner())

    def test_sum_of_unmarked(self):
        b = Board(['24 75 59 41 17',
                   '58 74 64 92 39',
                   '68  8 78 85 72',
                   '18  3 22  4 34',
                   '11 76  6 28 50'])
        b.mark_number('24')
        b.mark_number('74')
        b.mark_number('78')
        b.mark_number('4')
        b.mark_number('50')
        self.assertEqual(876, b.sum_of_unmarked())


if __name__ == '__main__':
    unittest.main()
