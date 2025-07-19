from dataclasses import dataclass
from matplotlib import pyplot as plt
import numpy as np

from viz import visualize_particle_system, visualize_particle_system_history, plot_parabola

N = 100

positions = np.zeros((N, 2))
velocities = np.zeros((N, 2))

# initial conditions
y0 = 100
v0 = 20

positions[:,] = (0, y0)

angles = np.linspace(0, np.pi*2, N, endpoint=False)
velocities[:,0] = v0*np.cos(angles)
velocities[:,1] = v0*np.sin(angles)


history = []

dt = 1e-3
g = 9.81

while np.any(positions[:,1] > 0):
    history.append(np.copy(positions))

    # apply gravity
    velocities[:,1] -= g * dt

    # integrate velocity
    positions += velocities * dt

    # ground collision
    positions[positions[:,1] < 0] = 0

# plot all trajectories
visualize_particle_system_history(history)

# bounding parabola from analytic solution
a=-g/(2*v0**2)
b=0
c=y0+v0**2/(2*g)
plot_parabola(a, b, c, color="black", lw=3, ls="--")

plt.show()


def parabaloid_volume(a, b, c):
    "volume of parabaloid of rotation bounded below by z=0"
    x0 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)

    V = 2 * np.pi * (
        (a/4) * x0**4 +
        (b/3) * x0**3 +
        (c/2) * x0**2
    )

    return V

V = parabaloid_volume(a, b, c)
print(round(V, 4))

# => 1856532.8455
