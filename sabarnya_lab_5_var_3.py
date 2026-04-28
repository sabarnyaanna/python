import numpy as np
import matplotlib.pyplot as plt
from math import sin


def plotfunc1(a, b, n, f):
    # Генеруємо n точок від a до b
    x = np.linspace(a, b, n)
    # Обчислюємо значення f для кожного x
    # Vectorize дозволяє передавати масив у звичайну функцію (як sin)
    vf = np.vectorize(f)
    y = vf(x)

    plt.plot(x, y, label=f.__name__)
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Приклад параметрів: n=100, a=0, b=10
    n = 100
    a, b = 0, 10

    # Використовуємо вбудований sin та власну лямбда-функцію
    funcs = [sin, lambda x: x ** 2 - 5 * x]
    for ff in funcs:
        plotfunc1(a, b, n, ff)