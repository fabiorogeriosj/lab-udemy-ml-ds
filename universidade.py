import pandas as pd

vagas = pd.read_csv('vagas_universidades.csv', delimiter='|')
municipios = pd.read_csv('Municipios_Brasileiros.csv', delimiter=';')

merge = pd.merge(vagas, municipios, on='municipio_ibge')

print(
    merge.head()
)
