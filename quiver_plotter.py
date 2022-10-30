import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.colors import Normalize

from config import Config


def plot(plot_data):
    prey_directions = plot_data['prey_directions']
    prey_positions = plot_data['prey_positions']
    predator_position = plot_data['predator_position']
    predator_direction = plot_data['predator_direction']
    filename = plot_data['filename']
    plot_label = plot_data['plot_label']

    plt.figure()
    plt.tight_layout()
    plt.xlabel("")
    plt.ylabel("")
    plt.xlim([0, Config.sim_dimensions[0]])
    plt.ylim([0, Config.sim_dimensions[1]])
    plt.tick_params(left=False, right=False, labelleft=False,
                    labelbottom=False, bottom=False)
    colormap = cm.viridis

    norm = Normalize()
    norm.autoscale(prey_directions)
    colors = colormap(norm(prey_directions))
    plt.quiver(prey_positions[0], prey_positions[1],
               np.cos(prey_directions), np.sin(prey_directions), color=colors, label=plot_label)
    plt.quiver(predator_position[0], predator_position[1], np.cos(predator_direction),
               np.sin(predator_direction), color='black')

    plt.legend(loc="upper left")
    plt.savefig(filename)# , dpi=150)# , bbox_inches='tight', pad_inches=0)
    plt.close()
