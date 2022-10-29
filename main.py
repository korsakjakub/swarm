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
    sw.get_initial_swarm(5000)
    colormap = cm.viridis
    norm = Normalize()
    for t_index in tqdm(range(200)):
        t = t_index * dt
        cur_sw = sw.new_positions()
        cur_dir = sw.new_directions()
        scatter_positions = np.array(cur_sw.get_positions(), dtype=object).T
        scatter_directions = cur_sw.get_directions().flatten()
        norm.autoscale(scatter_directions)
        fig = plt.figure()
        # plt.scatter(scatter_positions[0], scatter_positions[1])
        colors = colormap(norm(scatter_directions))
        plt.quiver(scatter_positions[0], scatter_positions[1],
                   np.cos(scatter_directions), np.sin(scatter_directions), color=colors)
        plt.xlabel("")
        plt.ylabel("")
        plt.xlim([0, Config.sim_dimensions[0]])
        plt.ylim([0, Config.sim_dimensions[1]])
        plt.tick_params(left=False, right=False, labelleft=False,
                        labelbottom=False, bottom=False)
        plt.title(f"t = {t_index}")
        plt.savefig(f"png/{str(t_index)}.png")
        plt.close()
    os.system('cd png; files=$(ls *.png | sort -n -k1); convert -delay 20 $files ../animation.gif; rm *.png')
