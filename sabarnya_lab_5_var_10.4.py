import numpy as np
import matplotlib.pyplot as plt
import math

a, b = -2, 2
m = 5
n_points = 500
n_monte_carlo = 50000

x = np.linspace(a, b, n_points)
f_x = np.exp(x)
f_approx = np.zeros_like(x)
for i in range(m):
    f_approx += (x**i) / math.factorial(i)

g_x = np.abs(f_x - f_approx)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ax1.plot(x, f_x, 'r', label='$f(x) = e^x$', linewidth=2)
ax1.plot(x, f_approx, 'b--', label=f'Наближення Тейлора (m={m})')
ax1.fill_between(x, f_x, f_approx, color='gray', alpha=0.3, label='Область помилки')

ax1.set_title('Порівняння функції та її наближення')
ax1.legend()
ax1.grid(True)
y_min, y_max = ax1.get_ylim()
x_min, x_max = ax1.get_xlim()
rect_area = (x_max - x_min) * (y_max - y_min)

ax2.plot(x, g_x, 'g', label='$g(x) = |f(x) - f_{approx}(x)|$')
ax2.fill_between(x, 0, g_x, color='green', alpha=0.2)
ax2.set_title('Графік модуля різниці (похибка)')
ax2.legend()
ax2.grid(True)
mc_x = np.random.uniform(x_min, x_max, n_monte_carlo)
mc_y = np.random.uniform(y_min, y_max, n_monte_carlo)
f_mc = np.exp(mc_x)
f_approx_mc = np.zeros_like(mc_x)
for i in range(m):
    f_approx_mc += (mc_x**i) / math.factorial(i)

inside = np.logical_and(mc_y > np.minimum(f_mc, f_approx_mc),
                        mc_y < np.maximum(f_mc, f_approx_mc))

error_area = (np.sum(inside) / n_monte_carlo) * rect_area
mean_error = np.sqrt(error_area / rect_area)

print(f"Площа охоплюючого прямокутника: {rect_area:.4f}")
print(f"Площа області помилки (Монте-Карло): {error_area:.4f}")
print(f"Середня похибка наближення: {mean_error:.4f}")

plt.tight_layout()
plt.show()