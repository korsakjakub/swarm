import numpy as np

from bird import Bird


class Prey(Bird):

    def new_direction(self, neighbour_directions, noise) -> float:
        self.direction = np.mean(neighbour_directions[self.index]) + self.a * 2 * np.pi * noise
        return self.direction

    def escape_predator(self, predator_position):
        rel_position = self.position - predator_position
        self.direction = np.arctan(rel_position[1] / rel_position[0])
        if rel_position[0] <= 0.0 and rel_position[1] <= 0.0:
            self.direction += np.pi
        # print(f'i: {self.index}, dir: {self.direction}')
        return self.direction
