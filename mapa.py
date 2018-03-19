import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset
from planilha.volume import csv, excel
import seaborn as sns

import locale
locale.setlocale(locale.LC_ALL, 'pt')

import mplleaflet

sns.set_style("darkgrid")

copacabana = pd.read_csv('copacabana_lat_lng.csv')
print(
    copacabana.head()
)
plt.scatter(copacabana['lng'], copacabana['lat'], marker='.')
mplleaflet.show()