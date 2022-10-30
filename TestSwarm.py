import unittest

import numpy as np

from predator import Predator
from prey import Prey
from swarm import Swarm


class TestSwarm(unittest.TestCase):
    def test_get_initial_swarm(self):
        sw = Swarm()
        init_swarm = sw.get_initial_swarm(10)
        self.assertEqual(len(init_swarm.birds), 10)
        for bird in init_swarm.birds:
            self.assertIsNotNone(bird.position)
            self.assertIsNotNone(bird.direction)
            self.assertEqual(type(bird.position), np.ndarray)
            self.assertEqual(type(bird.direction), np.float64)

    def test_get_nearest_neighbours(self):
        sw = Swarm(params={"r": 0.3})
        config = {"v0": 10}
        sw.birds = [Prey(position=np.array([0.1 * float(i), 0.0]), direction=0, params=config) for i in range(5)]
        got = sw.get_nearest_neighbours()
        want = {0: [1, 2], 1: [0, 2, 3], 2: [4, 1, 3, 0], 3: [4, 2, 1], 4: [2, 3]}
        for i in range(len(got)):
            self.assertTrue(
                np.allclose(np.sort(got[i]), np.sort(want[i])),
                msg=f"wanted: {want[i]} got: {got[i]}"
            )

    def test_mean_direction_of_neighbours(self):
        sw = Swarm(params={"r": 0.5})
        config = {"v0": 10}
        sw.birds = [Prey(position=np.array([0.1 * float(i), 0.0]), direction=float(i), params=config) for i in range(5)]
        mean_direction = sw.mean_direction_of_neighbours()
        want = {0: 2.5, 1: 2.25, 2: 2.0, 3: 1.75, 4: 1.5}
        self.assertDictEqual(mean_direction, want)

    def test_escape_predator(self):
        params = {"r": 0.5, "rb": 2, "v0": 10}
        sw = Swarm(params=params)
        sw.birds = [Prey(position=np.array([0.1 * float(i), float(i)]), direction=1, params=params) for i in range(5)]
        sw.predator = Predator(position=[0.25, 1.0], direction=0, params=params)
        sw.prey_escape_predator()
        print(sw.get_positions())


if __name__ == '__main__':
    unittest.main()
