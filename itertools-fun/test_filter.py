import unittest
import itertools


class FilterTestClass(unittest.TestCase):

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
            {'heading': 'Literature', 'duration': 1.0, 'id': 5},
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

    def get_courses(self):
        sorted_st_cl = sorted(self.students_classes, key=lambda r: r['class_id'])
        for class_id, students_classes in itertools.groupby(sorted_st_cl, lambda r: r['class_id']):
            class_heading = next(cl['heading'] for cl in self.classes if cl['id'] == class_id)
            student_ids = [student_class['student_id'] for student_class in students_classes]
            students = [next(st for st in self.students if st['id'] == st_id) for st_id in student_ids]
            yield Course(class_heading, students)

    # print out list of classes that contains at least 1 student 26 (or more) years old
    # starring: dropwhile (here `next` could be used as well)
    def test_dropwhile(self):
        courses = self.get_courses()
        for course in courses:
            old_students = itertools.dropwhile(lambda s: s['age'] < 26, course.students)
            if len(list(old_students)) > 0:
                print(course)
        assert 1 == 1

    # print out classes that do not have students
    # starring: filterfalse
    def is_there_a_student_for_class(self, class_id):
        try:
            next(st_cl for st_cl in self.students_classes if st_cl['class_id'] == class_id)
            return True
        except StopIteration:
            return False

    def test_filter(self):
        for empty_course in itertools.filterfalse(self.is_there_a_student_for_class, [cl['id'] for cl in self.classes]):
            print(empty_course)
        assert 1 == 1


class Course(object):
    def __init__(self, heading, students):
        self.heading = heading
        self.students = students

    def __repr__(self):
        return '{} students: {}'.format(self.heading, ', '.join([st['name'] for st in self.students]))


