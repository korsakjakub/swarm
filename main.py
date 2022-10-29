import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from tqdm import tqdm

from config import Config
from swarm import Swarm

if __name__ == '__main__':
    dt = Config.dt
    sw = Swarm()
    sw.get_initial_swarm(100)
    colormap = cm.viridis
    norm = Normalize()
    for t_index in tqdm(range(10)):
        t = t_index * dt
        cur_sw = sw.new_positions()
        cur_dir = sw.new_directions()
        cur_predator_direction = sw.new_predator_direction()
        cur_predator_position = sw.new_predator_position()
        sw.prey_escape_predator()
        scatter_positions = np.array(cur_sw.get_positions(), dtype=object).T
        scatter_directions = cur_sw.get_directions().flatten()
        norm.autoscale(scatter_directions)
        fig = plt.figure()
        colors = colormap(norm(scatter_directions))
        plt.quiver(scatter_positions[0], scatter_positions[1],
                   np.cos(scatter_directions), np.sin(scatter_directions), color=colors, label=f"t = {t_index}")
        #plt.quiver(cur_predator_position[0], cur_predator_position[1], np.cos(cur_predator_direction), np.sin(cur_predator_direction), color='black')
        plt.xlabel("")
        plt.ylabel("")
        plt.xlim([0, Config.sim_dimensions[0]])
        plt.ylim([0, Config.sim_dimensions[1]])
        plt.tick_params(left=False, right=False, labelleft=False,
                        labelbottom=False, bottom=False)
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.savefig(f"png/{str(t_index)}.png", dpi=150, bbox_inches='tight', pad_inches=0)
        plt.close()
    os.system('cd png; files=$(ls *.png | sort -n -k1); convert -delay 20 $files ../animation.gif; rm *.png')
