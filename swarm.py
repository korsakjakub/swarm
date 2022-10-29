import numpy as np
from numpy.random import default_rng
from scipy.spatial import cKDTree

from bird import Bird
from config import Config


class Swarm:
    def __init__(self, params=None):
        if params is None:
            params = {}
        self.neighbour_directions = None
        self.neighbours = None
        self.birds = []
        self.r = params["r"] if "r" in params else Config.r

    def __str__(self):
        return f'{self.birds}'

    def get_initial_swarm(self, amount):
        sim_dimensions = Config.sim_dimensions
        rng = np.random.default_rng()
        pos = sim_dimensions * rng.random((amount, 2))
        theta = 2 * np.pi * rng.random((amount, 1))
        self.birds = [Bird(pos[i], theta[i], index=i) for i in range(amount)]
        return self

    def get_nearest_neighbours(self):
        if len(self.birds) == 0:
            return None
        kd_tree = cKDTree(self.get_positions())
        pairs = kd_tree.query_pairs(r=self.r)
        neighbours = {i: [] for i in range(len(self.birds))}
        for (i, j) in pairs:
            neighbours[i].append(j)
            neighbours[j].append(i)
        self.neighbours = neighbours
        return neighbours

    def mean_direction_of_neighbours(self):
        mean_directions = {i: [] for i in range(len(self.birds))}
        nearest_neighbours = self.get_nearest_neighbours()
        for key in nearest_neighbours:
            nnk = nearest_neighbours[key]
            mean_directions[key] = np.sum([self.birds[nnk[i]].direction/len(nnk) for i in range(len(nnk))])
        self.neighbour_directions = mean_directions
        return mean_directions

    def new_positions(self):
        for i in range(len(self.birds)):
            self.birds[i].position = self.birds[i].new_position()
        return self

    def new_directions(self):
        self.mean_direction_of_neighbours()
        rng = np.random.default_rng()
        noise = rng.random(1)
        for i in range(len(self.birds)):
            self.birds[i].direction = self.birds[i].new_direction(self.neighbour_directions, noise)
        return self

    def get_positions(self):
        out = []
        birds = self.birds
        for bird in birds:
            out.append(bird.position)
        return np.array(out)

    def get_directions(self):
        out = []
        birds = self.birds
        for bird in birds:
            out.append(bird.direction)
        return np.array(out)


if __name__ == '__main__':
    sw = Swarm()
    sw.get_initial_swarm(200)
    nn = sw.get_nearest_neighbours()
    print(nn)
    print(sw.mean_direction_of_neighbours())
