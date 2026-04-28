import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

a, b = -3, 3
m = 15
x_values = np.linspace(a, b, 400)
y_original = np.exp(x_values)

fig, ax = plt.subplots(figsize=(10, 6))


def update(n):
    ax.clear()
    y_approx = np.zeros_like(x_values)
    for i in range(n):
        y_approx += (x_values ** i) / math.factorial(i)

    ax.plot(x_values, y_original, 'r', label='Оригінал: $e^x$', linewidth=2)
    ax.plot(x_values, y_approx, 'b--', label=f'Наближення (n={n} доданків)')


    ax.set_ylim(-1, 25)
    ax.set_title(f'Наближення функції $e^x$ рядом Тейлора (n = {n})')
    ax.legend(loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.7)

ani = FuncAnimation(fig, update, frames=range(1, m + 1), interval=500, repeat=True)
plt.show()