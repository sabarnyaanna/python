import numpy as np
import matplotlib.pyplot as plt

TEST_NUM = 100000


def trinomial(a, b, c):
    '''Повертає функцію для обчислення a*x**2 + b*x + c.'''
    return lambda x: a * x ** 2 + b * x + c


def exp1x(x):
    '''Функція exp(1/x).'''
    return np.exp(1 / x)


def get_box_bounds(a, b, c):
    '''Обчислює межі прямокутника, що охоплює область перетину.'''
    if a >= 0:
        raise ValueError(f'a = {a}. Має бути a < 0 (парабола гілками вниз).')

    # xmin вибираємо близько до 0, оскільки в 0 функція exp(1/x) прямує до нескінченності
    xmin = 0.4
    ymin = 0
    # Максимум параболи (вершина): y = c - b^2 / 4a
    ymax = c - b ** 2 / (4 * a) + 0.5

    # Знаходимо корінь параболи для xmax (наближено)
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        xmax = xmin + 2
    else:
        xmax = (-b - np.sqrt(discriminant)) / (2 * a) + 0.5

    return xmin, xmax, ymin, ymax


def mc_square(f1, f2, xmin, xmax, ymin, ymax):
    '''Обчислює площу між f1 та f2 методом Монте-Карло.'''
    # Генеруємо випадкові точки всередині прямокутника
    x_rand = np.random.uniform(xmin, xmax, TEST_NUM)
    y_rand = np.random.uniform(ymin, ymax, TEST_NUM)

    # Значення функцій у цих точках
    y1_val = f1(x_rand)
    y2_val = f2(x_rand)

    # Точка "всередині", якщо вона між кривими
    is_inside = (y_rand >= y1_val) & (y_rand <= y2_val)
    count_in = np.sum(is_inside)

    # Площа = (частка точок) * (площа прямокутника)
    box_area = (xmax - xmin) * (ymax - ymin)
    area = (count_in / TEST_NUM) * box_area

    return area, x_rand[is_inside], y_rand[is_inside]


def plot_result(a_in, b_in, c_in, xmin, xmax, ymin, ymax, f1, f2, area):
    '''Малює графіки та зафарбовує область.'''
    x = np.linspace(xmin, xmax, 500)
    y1 = f1(x)
    y2 = f2(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'r', label='exp(1/x)')
    plt.plot(x, y2, 'b', label='parabola')

    # Заливка області
    plt.fill_between(x, y1, y2, where=(y2 >= y1), color='cyan', alpha=0.3, label='Область площі')

    # Малюємо межі прямокутника Монте-Карло
    plt.rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                             fill=False, edgecolor='black', linestyle='--', label='Box')
    plt.gca().add_patch(plt.rect)

    plt.title(f"Площа між кривими (Monte Carlo): ≈ {area:.4f}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == '__main__':
    # Параметри для тесту: a=-2, b=8, c=1
    try:
        a_p, b_p, c_p = -2.0, 8.0, 1.0

        xmin, xmax, ymin, ymax = get_box_bounds(a_p, b_p, c_p)
        tri = trinomial(a_p, b_p, c_p)

        area, pts_x, pts_y = mc_square(exp1x, tri, xmin, xmax, ymin, ymax)

        print(f"Розрахункова площа: {area:.6f}")
        plot_result(a_p, b_p, c_p, xmin, xmax, ymin, ymax, exp1x, tri, area)

    except ValueError as e:
        print(f"Помилка: {e}")