import os

import numpy as np
from tqdm import tqdm

import quiver_plotter as qp
from config import Config
from swarm import Swarm


def simulate():
    sw = Swarm()
    sw.get_initial_swarm(Config.birds_amount, Config.include_predator)
    for t_index in tqdm(range(Config.time_range)):
        sw.new_directions()
        if Config.include_predator:
            sw.prey_escape_predator()
        cur_sw = sw.new_positions()
        if Config.include_predator:
            cur_predator_direction = sw.new_predator_direction()
            cur_predator_position = sw.new_predator_position()
        prey_positions = np.array(cur_sw.get_positions(), dtype=object).T
        prey_directions = cur_sw.get_directions()

        if Config.include_predator:
            qp.plot(plot_data={'prey_positions': prey_positions,
                               'prey_directions': prey_directions,
                               'predator_position': cur_predator_position,
                               'predator_direction': cur_predator_direction,
                               'filename': f'{Config.gif_dir}{str(t_index)}.png',
                               'plot_label': f't = {t_index}'
                               })
        else:
            qp.plot(plot_data={'prey_positions': prey_positions,
                               'prey_directions': prey_directions,
                               'filename': f'{Config.gif_dir}{str(t_index)}.png',
                               'plot_label': f't = {t_index}'
                               })

    os.system(f'cd {Config.gif_dir}; files=$(ls *.png | sort -n -k1); convert -delay 20 $files animation.gif; rm *.png')


if __name__ == '__main__':
    simulate()
