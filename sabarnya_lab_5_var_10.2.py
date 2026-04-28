import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 0.5
ks = np.arange(2, 11)
fig, ax = plt.subplots(figsize=(7, 7))

def update(frame_idx):
    ax.clear()
    k = ks[frame_idx]
    n = 2 ** k
    angles = np.linspace(0, 2 * np.pi, n + 1)
    x = R * np.cos(angles)
    y = R * np.sin(angles)
    side_length = 2 * R * np.sin(np.pi / n)
    pi_approx = n * side_length
    circle_angles = np.linspace(0, 2 * np.pi, 200)
    ax.plot(R * np.cos(circle_angles), R * np.sin(circle_angles), 'gray', linestyle='--', alpha=0.5)
    ax.plot(x, y, 'blue', marker='o', markersize=4, label=f'n = {n} (2^{k})')
    ax.fill(x, y, 'blue', alpha=0.1)
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect('equal')
    ax.set_title(f'Наближення π: {pi_approx:.6f}\n(Справжнє π ≈ 3.141593)', fontsize=12)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)


ani = FuncAnimation(fig, update, frames=len(ks), interval=1000, repeat=True)
plt.show()