import numpy as np

from bird import Bird


class Prey(Bird):

    def new_direction(self, neighbour_directions, noise) -> float:
        self.direction = np.angle(
            np.sum(np.exp(neighbour_directions[self.index] * 1j))) + self.a * 2 * np.pi * noise
        return self.direction

    def escape_predator(self, predator_direction):
        self.direction = predator_direction
        return self.direction
