#T120_01_v1
#Обчислення інтервалу значень вектору (для списків та масивів numpy)

# import numpy as np
# import random
#
# def interval(x):
#     '''Повертає різницю між максимальним та мінімальним елементом списку
#     '''
#     return max(x) - min(x)
#
# def np_interval(a):
#     '''Повертає різницю між максимальним та мінімальним елементом масиву numpy
#     '''
#     return np.max(a) - np.min(a)
#
#
#
# n = int(input('Кількість елементів: '))
#
# x = [random.random() for i in range(n)]
# print('створено список')
# print('інтервал', interval(x))
#
# a = np.array(x)
# print('створено масив numpy')
# print('numpy - інтервал', np_interval(a))



#T120_01_v2
#Обчислення інтервалу значень вектору (для списків та масивів numpy)
#Використовується декоратор benchmark для порівняння часу виконання

import time
import functools
import numpy as np
import random

# 1. Сам декоратор для вимірювання часу
def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[{func.__name__}] Час виконання: {end_time - start_time:.6f} сек")
        return result
    return wrapper

# 2. Ваші функції з декоратором
@benchmark
def interval(x):
    '''Повертає різницю між макс та мін елементом списку'''
    return max(x) - min(x)

@benchmark
def np_interval(a):
    '''Повертає різницю між макс та мін елементом масиву numpy'''
    return np.max(a) - np.min(a)

# 3. Виконання
n = int(input('Кількість елементів: '))

# Створюємо дані
x = [random.random() for i in range(n)]
a = np.array(x)

print(f"\nТестуємо для n = {n}:")
print('Інтервал (Python):', interval(x))
print('Інтервал (NumPy): ', np_interval(a))