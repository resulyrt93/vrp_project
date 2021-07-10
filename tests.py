import unittest
from copy import copy

from src.parser import MessageValidator, MessageParser
from src.route_solver import RouteSolver

dummy_data = {
    "vehicles": [
        {
            "id": 1,
            "start_index": 1,
            "capacity": [
                4
            ]
        },
        {
            "id": 2,
            "start_index": 0,
            "capacity": [
                2
            ]
        }
    ],
    "jobs": [
        {
            "id": 1,
            "location_index": 2,
            "delivery": [
                2
            ],
            "service": 123
        },
        {
            "id": 2,
            "location_index": 0,
            "delivery": [
                4
            ],
            "service": 453
        },
    ],
    "matrix": [
        [0, 213, 342, 432],
        [214, 0, 435, 123],
        [312, 413, 0, 675],
        [412, 112, 567, 0],
    ]
}


class TestValidator(unittest.TestCase):
    """
    Test class for MessageValidator class. There is two rule for validation:
        1. Message should have three keys => vehicles, jobs, matrix
        2. These values should be a list instance.
    """

    def test_not_validated_message_content(self):
        validator = MessageValidator(dummy_data)
        self.assertFalse(validator.validated, "Should be False initially")

    def test_validated_message_content(self):
        validator = MessageValidator(dummy_data)
        validator.validate()
        self.assertTrue(validator.validated)

    def test_not_proper_message_content(self):
        broken_dummy_data = copy(dummy_data)
        broken_dummy_data.pop("jobs")
        validator = MessageValidator(broken_dummy_data)

        self.assertRaises(Exception, validator.validate)


class TestParser(unittest.TestCase):
    """
    Test class for MessageParser class. Parser class contain some helper methods for
    destruct that message object more effective and safely.
    Test methods usually compare statically, output of parser method and values of dummy data
    """
    def __init__(self, *args, **kwargs):
        super(TestParser, self).__init__(*args, **kwargs)
        self.parser = MessageParser(data=dummy_data)

    def test_parser_vehicle_count_method(self):
        self.assertEqual(self.parser.get_vehicle_count(), len(dummy_data["vehicles"]))

    def test_dummy_location_index(self):
        self.assertEqual(len(self.parser.matrix), len(dummy_data["matrix"]) + 1)

    def test_location_index_to_jobs_ids(self):
        self.assertEqual(self.parser.get_job_ids_with_location_index(2), [1])

    def test_total_service_time_for_location_index(self):
        self.assertEqual(self.parser.get_total_service_time_with_location_index(0), 453)


class TestSolver(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSolver, self).__init__(*args, **kwargs)
        self.parser = MessageParser(data=dummy_data)

    def test_distance_callback(self):
        solver = RouteSolver(self.parser)
        solver.manager = solver.create_manager()
        self.assertEqual(solver.distance_callback(1, 2), 435 + 123)


if __name__ == '__main__':
    unittest.main()
