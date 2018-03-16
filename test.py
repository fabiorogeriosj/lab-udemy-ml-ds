from lib.mlerning import calc1, parse_file, parse_csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset
from database.vendas import db_vendas
from planilha.volume import csv, excel

import locale
locale.setlocale(locale.LC_ALL, 'pt')

#print(calc1(10))

data = parse_file('iris.data')
setosa = data[:50,0]
versicolor = data[50:100,0]

## utilizando plot
# plt.figure(figsize=(15,5))
# linestyles = ['-', '--', '-.', ':']
# plt.plot(setosa, c="Red", linestyle='-', marker='s', ls=':', ms=8, label="Comp. Sépala Iris-Setosa")
# plt.plot(versicolor, c="Green", linestyle='--', marker='o', ls=':', ms=8, label="Comp. Sépala Iris-Versicolor")
# plt.legend()
# plt.show()

# s = pd.Series(setosa)
df = pd.DataFrame(
    [
        ['fabio', 123],
        ['rogerio', 554],
        ['silva', 876]
    ],
    columns=['name', 'total']
)

#print(df.ix[:2])

# titanic = pydataset.data('titanic')

# print(titanic.head())
# print(titanic.tail())
# print(titanic.describe())
# data = parse_csv('vendas.csv')
# print(np.sum(data, axis=0))
#print(np.array_split([[1,2],[3,4],[5,6],[7,8]], 2, axis=0))

# print(
#     db_vendas().query('select * from pedidos')
# )

notas = excel('volume_notas.xlsx')
notas['Total'] = notas['NFCe'] + notas['NFe'] + notas['CTe'] + notas['NFSe'] + notas['SAT'] + notas['MDFe'] + notas['CTeOS'] + notas['GNRE']

# print(
#     notas.head()
# )

#locale.format("%d", 20456545, grouping=True)

total_por_ano = notas.groupby('Ano').aggregate({'Total': [sum]})
#total_por_mes = notas.groupby('Mês').aggregate({'Total': [sum]}).sort(['Mês'], descending=[1])

print(
    notas.head()
)

#print(np.zeros((2,2)))

#print(np.ones((10,10)))

#matrix identidade
#print(np.eye(10))
# array = np.genfromtxt('dataset.txt', filling_values=-1)
# print(array)

def teste_plot():
    data1 = np.array([100, 200, 140, 720, 333])
    data2 = np.array([72, 130, 50, 800, 343])
    data3 = np.array([80, 160, 70, 200, 143])

    plt.plot(data1, c='Black', ls='--', marker='s', ms=10, label="Data1")
    plt.plot(data2, c='Red', ls='--', marker='^', ms=10, label="Data2")
    plt.plot(data3, c='Green', ls='--', marker='o', ms=10, label="Data3")
    plt.legend(loc='upper left')
    plt.show()