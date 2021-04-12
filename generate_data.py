import numpy as np
import os


if __name__ == "__main__":
    # Read in random state from text-file
    with open("random_seed.txt") as rs_file:
        random_state = int(rs_file.read())

    # Generate huge random matrix
    X = np.random.RandomState(random_state).rand(1500, 1500)

    # Store the matrix
    np.savetxt(os.path.join("data", "X.csv"), X)
