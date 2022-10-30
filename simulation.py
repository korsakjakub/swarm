import os

import numpy as np
from tqdm import tqdm

import quiver_plotter as qp
from predator import Predator
from prey import Prey
from swarm import Swarm


def simulate():
#   config = {"a": 0.15, "rb": 5}
#   sw = Swarm(params=config)
#   sw.birds = [Prey(position=np.array([1.0 + float(i), 16.0]), direction=0, index=i, params=config) for i in range(5)]
#   sw.predator = Predator(position=[8.0, 16.0], direction=0, params=config)
    sw = Swarm({"rb": 8})
    sw.get_initial_swarm(10000)
    for t_index in tqdm(range(500)):
        sw.new_directions()
        sw.prey_escape_predator()
        cur_sw = sw.new_positions()
        cur_predator_direction = sw.new_predator_direction()
        cur_predator_position = sw.new_predator_position()
        prey_positions = np.array(cur_sw.get_positions(), dtype=object).T
        prey_directions = cur_sw.get_directions()

        qp.plot(plot_data={'prey_positions': prey_positions,
                           'prey_directions': prey_directions,
                           'predator_position': cur_predator_position,
                           'predator_direction': cur_predator_direction,
                           'filename': f'tmp/{str(t_index)}.png',
                           'plot_label': f't = {t_index}'
                           })
    os.system('cd tmp; files=$(ls *.png | sort -n -k1); convert -delay 20 $files ../web/static/animation.gif; rm *.png')


if __name__ == '__main__':
    simulate()
