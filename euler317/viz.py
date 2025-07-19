from matplotlib import pyplot as plt
import numpy as np

def visualize_particle_system(positions, velocities, xlim=(-110, 110), ylim=(0, 200)):
    plt.plot(positions[:,0], positions[:,1])
    plt.xlim(*xlim)
    plt.ylim(*ylim)

def visualize_particle_system_history(positions_list, xlim=(-110, 110), ylim=(0, 130)):
    history = np.array(positions_list)

    T, N, _ = history.shape

    for i in range(N):
        plt.plot(history[:,i,0], history[:,i,1])

    # plt.axis("equal")

    plt.xlim(*xlim)
    plt.ylim(*ylim)

    plt.gca().set_aspect('equal', adjustable='box')


def plot_parabola(a, b, c, **kwargs):
    x = np.linspace(-100, 100, 1000)
    y = a*x**2 + b*x + c

    plt.plot(x, y, **kwargs)