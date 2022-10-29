import numpy as np
from config import Config


class Bird:
    def __init__(self, position, direction, index=None, params=None):
        if params is None:
            params = {}
        self.position = position
        self.direction = direction
        if index is not None:
            self.index = index
        self.v0 = params["v0"] if "v0" in params else Config.v0
        self.dt = params["dt"] if "dt" in params else Config.dt
        self.sim_dimensions = params["sim_dimensions"] if "sim_dimensions" in params else Config.sim_dimensions
        self.a = params["a"] if "a" in params else Config.a

    def __str__(self):
        return f'{self.position}, {self.direction}'

    def new_position(self) -> float:
        new = np.add(self.position,
                     np.array(
                         [self.v0 * self.dt * np.cos(self.direction),
                          self.v0 * self.dt * np.sin(self.direction)]).reshape(
                         (2,)))
        if new[0] > self.sim_dimensions[0]:
            new[0] -= self.sim_dimensions[0]
        if new[1] > self.sim_dimensions[0]:
            new[1] -= self.sim_dimensions[0]
        if new[0] < 0.0:
            new[0] += self.sim_dimensions[0]
        if new[1] < 0.0:
            new[1] += self.sim_dimensions[0]
        self.position = new
        return self.position
