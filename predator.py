import numpy as np

from bird import Bird


class Predator(Bird):

    def new_direction(self, prey_position) -> float:
        rng = np.random.default_rng()
        noise = rng.random(1) - 0.5
        if prey_position is None:
            self.direction += self.a * noise
            return self.direction
        rel_position = prey_position - self.position
        self.direction = np.arctan(rel_position[1] / rel_position[0]) + self.a * 2 * np.pi * noise
        return self.direction
