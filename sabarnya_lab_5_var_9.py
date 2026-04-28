import numpy as np
import matplotlib.pyplot as plt
import os

# Створюємо папку для кадрів, якщо її немає
if not os.path.exists('tmp'):
    os.makedirs('tmp')


def simulate_gas_diffusion(nd, steps_total, a, b, x1, m=100):
    # 1. Початкове розташування в лівій частині (0 < x < x1)
    # Використовуємо новий генератор rng для стабільності
    rng = np.random.default_rng()
    x = rng.integers(0, x1 + 1, nd).astype(float)
    y = rng.integers(0, b + 1, nd).astype(float)

    # Можливі кроки: вліво, вправо, вгору, вниз
    directions = np.array([[-1, 0], [1, 0], [0, 1], [0, -1]])

    plt.ion()  # Увімкнути інтерактивний режим для анімації
    fig, ax = plt.subplots(figsize=(8, 5))

    frame_count = 0
    for s in range(0, steps_total + 1, m):
        ax.clear()
        ax.scatter(x, y, s=5, color='royalblue', alpha=0.6)
        ax.set_xlim(-1, a + 1)
        ax.set_ylim(-1, b + 1)
        ax.set_title(f"Крок: {s} | Ентропія зростає...")

        # Збереження кадру
        plt.savefig(f'tmp/frame_{frame_count:04d}.png')
        frame_count += 1
        plt.pause(0.1)

        if s < steps_total:
            # Робимо m кроків для кожної молекули одночасно (векторизація)
            for _ in range(m):
                step_ids = rng.integers(0, 4, nd)
                moves = directions[step_ids]
                x += moves[:, 0]
                y += moves[:, 1]

                # Обмеження стінками контейнера (відбиття)
                x = np.clip(x, 0, a)
                y = np.clip(y, 0, b)

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    # Параметри: 1000 молекул, контейнер 100x50, старт у перших 20 одиницях довжини
    simulate_gas_diffusion(nd=1000, steps_total=2000, a=100, b=50, x1=20, m=100)