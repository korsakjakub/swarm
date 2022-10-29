import logging
import unittest

import numpy as np

from prey import Prey
from swarm import Swarm


class TestSwarm(unittest.TestCase):
    def test_get_initial_swarm(self):
        sw = Swarm()
        init_swarm = sw.get_initial_swarm(10)
        logging.info(init_swarm.get_positions())

    def test_get_nearest_neighbours(self):
        sw = Swarm(params={"r": 0.3})
        config = {"v0": 10}
        sw.birds = [Prey(position=np.array([0.1 * float(i), 0.0]), direction=0, params=config) for i in range(5)]
        got = sw.get_nearest_neighbours()
        want = {0: [1, 2], 1: [0, 2, 3], 2: [4, 1, 3, 0], 3: [4, 2, 1], 4: [2, 3]}
        for i in range(len(got)):
            if not np.array_equal(np.sort(got[i]), np.sort(want[i])):
                logging.error("wanted: ", want[i], " got: ", got[i])

    def test_mean_direction_of_neighbours(self):
        sw = Swarm(params={"r": 0.5})
        config = {"v0": 10}
        sw.birds = [Prey(position=np.array([0.1 * float(i), float(i)]), direction=1, params=config) for i in range(5)]
        mean_direction = sw.mean_direction_of_neighbours()
        print(mean_direction)


if __name__ == '__main__':
    unittest.main()
