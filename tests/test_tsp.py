import os
import unittest

from tsp import TSP


def get_problem(name):
    """Get the fullpath to the TSP.

    :param name: name of the TSP
    :type name: str
    :return: fullpath to the TSP
    :rtype: str
    """
    return os.path.join(
        os.path.abspath(os.path.dirname(__file__)), f"{name}.csv"
    )


class TestTSP(unittest.TestCase):
    def test_nearest_neighbor(self):
        """Test the nearest neighbour algorithm.
        """
        # Test Cases
        tests = [
            {
                "start": 0,
                "result": [0, 4, 1, 2, 5, 3],
                "problem": "rheinlandproblem",
            },
            {
                "start": 3,
                "result": [3, 1, 4, 2, 5, 0],
                "problem": "rheinlandproblem",
            },
        ]

        # Iterate through the tests
        for test in tests:
            # Load test
            tsp = TSP.load(get_problem(test["problem"]))
            # Solve test and check result
            self.assertEqual(
                tsp.nearest_neighbor(test["start"]), test["result"]
            )
