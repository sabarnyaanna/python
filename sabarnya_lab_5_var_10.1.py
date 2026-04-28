import numpy as np
import matplotlib.pyplot as plt

def get_a(n):
    numerator = np.cbrt(2*n**4 + n**3 + 1) - n * np.cbrt(2*n + 3)
    denominator = np.cbrt(n + 1)
    return numerator / denominator

n_values = np.arange(1, 1001)
a_values = get_a(n_values)
b = -0.41997
epsilon = 0.01
k = -1
for i in range(len(a_values)):
    if np.all(np.abs(a_values[i:] - b) < epsilon):
        k = n_values[i]
        break

plt.figure(figsize=(12, 7))
plt.scatter(n_values, a_values, color='blue', s=8, label='Елементи $a_n$')
plt.axhline(y=b, color='red', linewidth=2, label=f'Границя $b \\approx {b:.4f}$')

plt.axhline(y=b + epsilon, color='green', linestyle='--', alpha=0.6, label=fr'Межа $b + \epsilon$')
plt.axhline(y=b - epsilon, color='green', linestyle='--', alpha=0.6, label=fr'Межа $b - \epsilon$')
plt.fill_between(n_values, b - epsilon, b + epsilon, color='green', alpha=0.15)

plt.title(f'Перевірка границі: елементи потрапляють у смугу при $n > {k}$', fontsize=14)
plt.xlabel('Номер елемента $n$')
plt.ylabel('Значення $a_n$')
plt.ylim(b - 0.1, b + 0.1)

plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.7)

plt.show()

print(f"Гіпотетична границя b = {b}")
if k != -1:
    print(f"Умова |a_n - b| < {epsilon} виконується для всіх n > {k}")
else:
    print("Умова не виконується на цьому проміжку, спробуйте збільшити n_values.")