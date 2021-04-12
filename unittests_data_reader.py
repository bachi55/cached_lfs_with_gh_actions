import unittest
import numpy as np
import os


class TestDataReader(unittest.TestCase):
    def test_loaded_data_is_correct(self):
        # Read the random state
        with open("random_seed.txt") as rs_file:
            random_state = int(rs_file.read())

        X_ref = np.random.RandomState(random_state).rand(1500, 1500)
        X = np.genfromtxt(os.path.join("data", "X.csv"))

        np.testing.assert_array_equal(X_ref, X)


if __name__ == '__main__':
    unittest.main()
