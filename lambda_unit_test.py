# Trying out lambda functions

import pytest
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

print(network_operations.sorted_students)

#below function is used for unit_testing

def test_sorted_students(sample_students):
    student_operations = StudentOperations(sample_students)
    sorted_students = student_operations.sorted_students

    assert sorted_students == [("Jack", 50), ("Jane", 75), ("John", 100)]
