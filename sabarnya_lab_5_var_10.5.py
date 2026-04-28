import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def lagrange_poly(x_eval, x_nodes, y_nodes):
    n = len(x_nodes)
    p_val = np.zeros_like(x_eval)

    for k in range(n):
        l_k = np.ones_like(x_eval)
        for i in range(n):
            if i != k:
                l_k *= (x_eval - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
        p_val += y_nodes[k] * l_k
    return p_val

ks = [2, 3, 4, 5]
x_fine = np.linspace(0, 2 * np.pi, 500)
y_true = np.sin(x_fine)
fig, ax = plt.subplots(figsize=(10, 6))

def update(k):
    ax.clear()
    n = 2 ** k
    x_nodes = np.linspace(0, 2 * np.pi, n + 1)
    y_nodes = np.sin(x_nodes)
    y_poly = lagrange_poly(x_fine, x_nodes, y_nodes)

    ax.plot(x_fine, y_true, 'gray', linestyle='--', alpha=0.5, label='sin(x)')
    ax.plot(x_fine, y_poly, 'blue', label=f'Поліном Лагранжа (k={k}, n={n})')
    ax.scatter(x_nodes, y_nodes, color='red', s=30, zorder=3, label='Вузли')

    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'Інтерполяція Лагранжа для sin(x)\nКількість вузлів: {n + 1}')
    ax.legend(loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.6)

ani = FuncAnimation(fig, update, frames=ks, interval=1500, repeat=True)
plt.show()