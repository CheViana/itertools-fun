import unittest
import itertools


class GroupTestClass(unittest.TestCase):

    def setUp(self):
        self.students = [
            {'name': 'Ann', 'age': 25, 'id': 0},
            {'name': 'Barbara', 'age': 26, 'id': 1},
            {'name': 'Clara', 'age': 25, 'id': 2},
            {'name': 'Diana', 'age': 24, 'id': 3},
            {'name': 'Eva', 'age': 27, 'id': 4},
        ]
        self.classes = [
            {'heading': 'Math', 'duration': 1.0, 'id': 0},
            {'heading': 'Physics', 'duration': 2.0, 'id': 1},
            {'heading': 'English', 'duration': 1.5, 'id': 2},
            {'heading': 'Biology', 'duration': 2.5, 'id': 3},
            {'heading': 'Chemistry', 'duration': 1.5, 'id': 4},
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

    # print out list of students for each class

    # version 1: map then group
    # starring: next, starmap, groupby
    def full_record_student_class(self, student_id, class_id):
        student_name = next(st['name'] for st in self.students if st['id'] == student_id)
        class_name = next(cl['heading'] for cl in self.classes if cl['id'] == class_id)
        return {'student_name': student_name, 'class_name': class_name, 'class_id': class_id, 'student_id': student_id}

    def test_startmap_groupby(self):
        ids = [(record['student_id'], record['class_id'],) for record in self.students_classes]
        # ids == [(0, 0), (1, 0), (3, 1), (2, 1), (0, 2), (4, 2), (2, 3), (4, 4)]
        # map
        ids_sorted = sorted(ids, key=lambda i: i[1])
        full_records = itertools.starmap(self.full_record_student_class, ids_sorted)
        # then group
        for class_name, students in itertools.groupby(full_records, lambda r: r['class_name']):
            c = Course(class_name, [student['student_name'] for student in students])
            assert c is not None

    # version 2: group
    # starring: groupby, next
    def test_groupby_map(self):
        sorted_st_cl = sorted(self.students_classes, key=lambda r: r['class_id'])
        for class_id, students_classes in itertools.groupby(sorted_st_cl, lambda r: r['class_id']):
            class_heading = next(cl['heading'] for cl in self.classes if cl['id'] == class_id)
            student_ids = [student_class['student_id'] for student_class in students_classes]
            student_names = [next(st['name'] for st in self.students if st['id'] == st_id) for st_id in student_ids]
            c = Course(class_heading, student_names)
            assert c is not None
        # assert 1 == 2   # just to see print in console


class Course(object):
    def __init__(self, heading, students):
        self.heading = heading
        self.students = students

    def __repr__(self):
        return '{} students: {}'.format(self.heading, ', '.join(self.students))


