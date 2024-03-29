# Trying out lambda functions

import pytest
import os
from unittest import TestCase, mock

def work_on():
    path = os.getcwd()
    print(f"Working on {path}")
    return path


@pytest.fixture
def sample_students():
    return [
        ("John", 100),
        ("Jack", 50),
        ("Jane", 75)
    ]

class StudentOperations(object):
    def __init__(self, students):
        self.students = students

    @property
    def sorted_students(self):
      sorted_list = sorted(self.students, key=lambda student: student[1])
      return sorted_list


network_operations = StudentOperations([
    ("John", 100),
    ("Jack", 50),
    ("Jane", 75)])

print(work_on())
print(network_operations.sorted_students)

#below function is used for unit_testing

def test_sorted_students(sample_students):
    student_operations = StudentOperations(sample_students)
    sorted_students = student_operations.sorted_students

    assert sorted_students == [("Jack", 50), ("Jane", 75), ("John", 100)]

class TestWorkingPath(TestCase):

    """
    def test_work_on(self):
        with mock.patch('lambda_unit_test.os') as mocked_os:
            work_on()
            mocked_os.getcwd.assert_called_once()
    """ 

    @mock.patch('lambda_unit_test.os.getcwd')
    def test_work_on(self, mocked_os_value):
        mocked_os_value.return_value = 'test_path'
        expected_path = work_on()
        assert expected_path == 'test_path'