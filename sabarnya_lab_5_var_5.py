# #T20_51_v1
# #Кидання костей. Ймовірність одночасного випадання шісток.
# #Метод Монте-Карло
#
#
# #import numpy as np
# #import matplotlib.pyplot as plt
# import random
#
# TEST_NUM = 10000
#
# def ndice_six_prob(ndice, nroll):
#     '''Обчислює ймовірність одночасного випадання ndice шісток у nroll киданнях.
#
#     '''
#     #dices - тривимірний масив випадкових результатів кидань костей від 1 до 6
#     #Перший вимір - кількість випробувань TEST_NUM
#     #Другий вимір - кількість кидань nroll
#     #Третій вимір - кількість костей ndice
#     dices =[ [ [random.randint(1, 6) for k in range(ndice)]
#                for j in range(nroll)] for i in range(TEST_NUM)]
#     print(dices)
#     #sixes - масив з ndice 6
#     sixes = [6] * ndice
#     #sixcount - масив кількостей комбінацій з ndice самих шісток
#     #для кожного окремого випробування з nroll кидань
#     sixcount = [ rolls.count(sixes) for rolls in dices]
#     print(sixcount)
#     #фільтруємо ті елементи sixcount, в яких
#     #кількість комбінацій з ndice самих шісток більше 0
#     #success - число таких елементів
#     success = len(list(filter(lambda cnt: cnt > 0, sixcount)))
#    print(success)
#     return success / TEST_NUM
#
#
# ndice = int(input('Кількість костей: '))
# nroll = int(input('максимальна кількість кидань: '))
#
# for rolls in range(1,nroll+1):
#     print('Ймовірність випадання {} 6 у {} киданнях = {}'.format(ndice,
#                     rolls, ndice_six_prob(ndice, rolls)))
#


import numpy as np

# Кількість експериментів Монте-Карло
TEST_NUM = 100000


def ndice_six_prob(ndice, nroll):
    """
    Обчислює ймовірність того, що хоча б один раз у nroll спробах
    випадуть одночасно ndice шісток.
    """
    # 1. Генеруємо випадкові числа від 1 до 6
    # Новий спосіб генерації: randint(low, high) генерує [low, high)
    dices = np.random.randint(1, 7, size=(TEST_NUM, nroll, ndice))

    # 2. Перевіряємо, де всі кубики в одному киданні дорівнюють 6
    # axis=2 — це вісь окремого кидання (ndice кубиків)
    all_sixes = np.all(dices == 6, axis=2)

    # 3. Перевіряємо, чи була хоча б одна успішна спроба у серії nroll
    # axis=1 — це вісь серії кидань
    success_in_series = np.any(all_sixes, axis=1)

    # 4. Рахуємо частку успішних серій серед усіх тестів
    return np.mean(success_in_series)


if __name__ == '__main__':
    try:
        ndice = int(input('Кількість костей: '))
        nroll_max = int(input('Максимальна кількість кидань у серії: '))

        print(f"\nМоделювання для {ndice} кубиків (Монте-Карло, {TEST_NUM} тестів):")
        for rolls in range(1, nroll_max + 1):
            prob = ndice_six_prob(ndice, rolls)
            print(f"Спроб: {rolls:2} | Ймовірність: {prob:.6f}")

    except ValueError:
        print("Помилка: введіть цілі числа.")

import numpy as np
import matplotlib.pyplot as plt

TEST_NUM = 10000


def draw_histogram(dices, sums, ndice, nroll):
    '''Зображує гістограми розподілу результатів випробувань.'''

    # Обчислюємо суму значень кубиків у кожному киданні
    n_sums_values = np.sum(dices, axis=1)

    plt.figure(figsize=(12, 5))

    # Ліва гістограма: Розподіл сум значень усіх кубиків
    plt.subplot(1, 2, 1)
    # Кількість бінів відповідає діапазону можливих сум: від ndice*1 до ndice*6
    bins_count = 6 * ndice - ndice + 1
    plt.hist(n_sums_values, bins=bins_count, color='salmon', edgecolor='black', alpha=0.7)
    plt.xlabel(f"Сума {ndice} костей")
    plt.ylabel("Частота")
    plt.title("Розподіл сум значень")

    # Права гістограма: Кількість успішних випадінь шісток у серіях
    plt.subplot(1, 2, 2)
    max_successes = np.max(sums)
    # Якщо успіхів не було, малюємо порожній графік, інакше встановлюємо біни
    bins_right = np.arange(max_successes + 2) - 0.5 if max_successes > 0 else 1
    plt.hist(sums, bins=bins_right, color='seagreen', edgecolor='black', alpha=0.7)
    plt.xlabel(f"Кількість комбінацій '{ndice} шісток'")
    plt.ylabel("Частота")
    plt.title(f"Успіхи у серіях по {nroll} кидань")

    plt.tight_layout()
    plt.show()


def ndice_six_prob(ndice, nroll, show_hist=False):
    '''Метод Монте-Карло для обчислення ймовірності випадання шісток.'''

    # Генеруємо результати кидань: TEST_NUM експериментів, у кожному nroll спроб по ndice кубиків
    # Використовуємо randint(1, 7), оскільки 7 не включається
    dices_raw = np.random.randint(1, 7, size=(TEST_NUM * nroll, ndice))

    # Масив булевих значень: чи є кидання успішним (всі ndice кубиків == 6)
    is_all_sixes = np.all(dices_raw == 6, axis=1)

    # Переформатовуємо у (експерименти, спроби)
    success_grid = is_all_sixes.reshape(TEST_NUM, nroll)

    # Рахуємо кількість успіхів у кожному з TEST_NUM експериментів
    sums_per_test = np.sum(success_grid, axis=1)

    if show_hist:
        draw_histogram(dices_raw, sums_per_test, ndice, nroll)

    # Успішним вважаємо експеримент, де хоча б раз випала потрібна комбінація
    success_count = np.count_nonzero(sums_per_test > 0)
    return success_count / TEST_NUM


if __name__ == '__main__':
    try:
        ndice = int(input('Кількість костей: '))
        nroll = int(input('Максимальна кількість кидань: '))

        for rolls in range(1, nroll + 1):
            # Показуємо гістограму тільки для останньої ітерації
            is_last = (rolls == nroll)
            prob = ndice_six_prob(ndice, rolls, is_last)
            print(f"Ймовірність {ndice} шісток у {rolls} киданнях = {prob:.6f}")

    except ValueError:
        print("Введіть коректні цілі числа.")





