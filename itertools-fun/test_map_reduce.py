import unittest
import functools
import itertools
import operator


class MapReduceTestClass(unittest.TestCase):

    def setUp(self):
        self.students = [
            {'name': 'Ann', 'age': 25, 'id': 0},
            {'name': 'Barbara', 'age': 26, 'id': 1},
            {'name': 'Clara', 'age': 25, 'id': 2},
            {'name': 'Diana', 'age': 24, 'id': 3},
            {'name': 'Eva', 'age': 27, 'id': 4},
        ]
        self.classes = [
            {'heading': 'math', 'duration': 1.0, 'id': 0},
            {'heading': 'physics', 'duration': 2.0, 'id': 1},
            {'heading': 'English', 'duration': 1.5, 'id': 2},
            {'heading': 'biology', 'duration': 2.5, 'id': 3},
            {'heading': 'chemistry', 'duration': 1.5, 'id': 4},
        ]
        self.students_classes = [
            {'student_id': 0, 'class_id': 0},
            {'student_id': 0, 'class_id': 1},
            {'student_id': 1, 'class_id': 3},
            {'student_id': 1, 'class_id': 2},
            {'student_id': 2, 'class_id': 0},
            {'student_id': 2, 'class_id': 4},
            {'student_id': 3, 'class_id': 2},
            {'student_id': 4, 'class_id': 4},
        ]

    # computing the average (or sum) age of students
    # starring: reduce, accumulate, map

    # reduce
    def test_average_age_by_reduce(self):
        ages = [student['age'] for student in self.students]
        sum_age = functools.reduce(lambda x,y: x+y, ages)
        assert sum_age == 127

    # accumulate
    def test_average_age_by_accumulate(self):
        ages = [student['age'] for student in self.students]
        sum_ages = itertools.accumulate(ages, func=operator.add)
        # sum_ages == [25, 51, 76, ... ]
        total_sum_age = list(sum_ages)[-1]
        assert total_sum_age == 127

    # map & reduce
    def test_average_age_by_map_reduce(self):
        students_amount = len(self.students)
        mapped_ages = map(lambda st: st['age']/students_amount, self.students)
        avg_age = functools.reduce(lambda x,y: x+y, mapped_ages)
        assert avg_age == 25.4








