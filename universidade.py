import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as dates
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

sns.set()

vagas = pd.read_csv('vagas_universidades.csv', delimiter='|')
municipios = pd.read_csv('Municipios_Brasileiros.csv', delimiter=';')

merge = pd.merge(vagas, municipios, on='municipio_ibge')
group = merge.groupby(['ano','UF'])[['valor']].sum()
group_anos = merge.groupby(['ano'])[['valor']].sum()
group_uf = merge.groupby(['UF'])[['valor']].sum()
print(group_uf)

group['ano'] = group.index.get_level_values(0)
group['uf'] = group.index.get_level_values(1)

filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
index = 0
for ano in group_anos.index:
    data = group.loc[group['ano'] == ano]
    plt.bar(ano, data['valor'], label=data['uf'])
    #plt.plot(data['uf'], data['valor'], filled_markers[index]+'-')
    index=index+1

plt.legend(group_uf.index)
    
plt.show()