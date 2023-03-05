from unittest.mock import Mock,patch
import unittest

def hello_world():
    msg = "Hello welcome to DPG automation"
    return msg

def calculate_length(l):
    return len(l)

class Calculation:
    def calculator_use_case(self,a,b):
        return a + b

class TestUseCase(unittest.TestCase):
    def test_hello_world_wrong(self):
        actual_result = hello_world()
        expected_result = "Hello welcome to DPG automation"
        assert actual_result == expected_result

    @patch("basic_unittest.calculate_length")
    def test_calulate_length(self,mock_value):
        mock_value.len = Mock()
        mock_value.return_value = 4
        actual_result = mock_value([2])
        assert actual_result == 4

    @patch(
        "basic_unittest.Calculation.calculator_use_case")
    def test_calculator_side_effect(self,mock_sum):
        mock_sum.side_effect = [4, 9]
        actual_result = mock_sum(2, 3)
        second_result = mock_sum(6, 7)
        assert actual_result == 4
        assert second_result == 9


if __name__ == '__main__':
    unittest.main()
