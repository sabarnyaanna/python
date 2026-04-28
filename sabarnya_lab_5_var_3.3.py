import numpy as np
import matplotlib.pyplot as plt
from math import sin


def movespinesticks():
    '''Центрує осі X та Y у точці (0,0) та прибирає зайві рамки'''
    ax = plt.gca()
    # Прибираємо верхню та праву межі рамки
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    # Переносимо нижню вісь (X) та ліву вісь (Y) у нуль
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    # Розміщуємо мітки (ticks) тільки на лівій та нижній осях
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')


def plotfunc4(a, b, n, *funcs):
    '''Малює кожну функцію у власному підграфіку з центрованими осями'''
    m = len(funcs)
    x = np.linspace(a, b, n)

    # Створюємо фігуру з динамічною висотою залежно від кількості функцій
    plt.figure(figsize=(8, 4 * m))

    for i, f in enumerate(funcs):
        # Створюємо підграфік: m рядків, 1 стовпець, i+1 позиція
        plt.subplot(m, 1, i + 1)

        # Обчислення значень
        vf = np.vectorize(f)
        y = vf(x)

        # Візуалізація
        plt.plot(x, y, linewidth=2, label=f.__doc__.strip() if f.__doc__ else f"f{i + 1}")
        movespinesticks()

        plt.title(f"Графік {i + 1}", loc='right', fontsize=10)
        plt.legend(loc='upper right')
        plt.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()  # Автоматичне вирівнювання відступів
    plt.show()


def fun(x):
    '''cos(x)'''
    return np.cos(x)


def sindivx(x):
    '''sin(x)/x'''
    return 1.0 if x == 0 else sin(x) / x


if __name__ == '__main__':
    # Приклад: n=200, a=-10, b=10
    try:
        n = 200
        a, b = -10, 10
        plotfunc4(a, b, n, fun, sindivx)
    except Exception as e:
        print(f"Сталася помилка: {e}")