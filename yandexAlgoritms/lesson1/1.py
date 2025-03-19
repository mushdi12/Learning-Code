import numpy as np
import pandas as pd

# Определяем функцию
def f(x):
    return -1.38*x**3 - 5.42*x**2 + 2.57*x + 10.95

def fx(x):
    return -4.14*x**2 - 10.84*x + 2.57    

# Задаем диапазон значений x с шагом 0.5
x_values = np.arange(-4, 2.5, 0.5)
f_values = [f(x) for x in x_values]

# Создаем таблицу значений
table = pd.DataFrame({'x': x_values, 'f(x)': f_values})
#print(table)
print(fx(1.5))