import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset
from planilha.volume import csv, excel
import seaborn as sns

import locale
locale.setlocale(locale.LC_ALL, 'pt')

sns.set_style("darkgrid")

incidencias = pd.read_csv('series_historicas.csv', delimiter='|')
print(incidencias.head())
plt.plot(incidencias['Ano'], incidencias['Total'])
plt.show()

# populacao = pd.read_csv('populacao_pib.csv', delimiter='|')
# populacao['Porcentagem'] = populacao['População'] / populacao['População'].sum()

# #plt.pie(populacao['Porcentagem'], labels=populacao['Sigla'])
# plt.show()