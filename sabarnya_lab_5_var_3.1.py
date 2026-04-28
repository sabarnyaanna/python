import numpy as np
import matplotlib.pyplot as plt
from math import sin


def plotfunc2(a, b, n, *funcs):
    # Генеруємо вісь X один раз для всіх функцій
    x = np.linspace(a, b, n)

    for f in funcs:
        # Векторизуємо функцію, щоб вона могла приймати масив x
        vf = np.vectorize(f)
        y = vf(x)

        # Малюємо лінію та додаємо назву функції в легенду
        plt.plot(x, y, label=f.__name__ if hasattr(f, '__name__') else "function")

    plt.axhline(0, color='black', linewidth=0.5)  # Вісь X
    plt.axvline(0, color='black', linewidth=0.5)  # Вісь Y
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.title(f"Графік функцій на інтервалі [{a}, {b}]")
    plt.show()


def sindivx(x):
    '''Sinc функція: sin(x)/x'''
    return 1.0 if x == 0 else sin(x) / x


def example_poly(x):
    '''Приклад полінома: x^2 - 4'''
    return x ** 2 - 4


if __name__ == '__main__':
    # Параметри для тесту: n=200, a=-10, b=10
    n = 200
    a, b = -10, 10

    # Список функцій для зображення
    funcs_list = [sindivx, example_poly]

    # Виклик з розпакуванням списку
    plotfunc2(a, b, n, *funcs_list)