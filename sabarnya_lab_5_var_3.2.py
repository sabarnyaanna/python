import numpy as np
import matplotlib.pyplot as plt
from math import sin

# Стилі та кольори для розрізнення ліній
styles = ['-', '--', '-.', ':']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']


def plotfunc3(a, b, n, *funcs):
    """Зображує графіки функцій *funcs з легендою та стилізацією"""
    x = np.linspace(a, b, n)
    legend_labels = []

    for i, f in enumerate(funcs):
        # Вибираємо стиль: комбінація типу лінії та кольору (напр. '-b')
        style = styles[i % len(styles)] + colors[i % len(colors)]

        # Обчислюємо Y (vectorize дозволяє працювати зі звичайними функціями)
        y = np.vectorize(f)(x)

        # Малюємо графік
        plt.plot(x, y, style)

        # Додаємо опис із docstring у список для легенди
        label = f.__doc__.strip() if f.__doc__ else f"function {i + 1}"
        legend_labels.append(label)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(legend_labels)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()


def fun(x):
    """cos(x)"""
    return np.cos(x)


def sindivx(x):
    """sin(x)/x"""
    return 1.0 if x == 0 else sin(x) / x


if __name__ == '__main__':
    # Введення даних (приклад: n=100, a=0, b=7)
    try:
        n = int(input('Кількість точок: '))
        a = float(input('Початок відрізку: '))
        b = float(input('Кінець відрізку: '))

        plt.title('Порівняння cos(x) та sin(x)/x')

        # Встановлюємо межі осей: [xmin, xmax, ymin, ymax]
        plt.axis([a, b, -1.5, 1.5])

        plotfunc3(a, b, n, fun, sindivx)
    except ValueError:
        print("Будь ласка, введіть коректні числа.")