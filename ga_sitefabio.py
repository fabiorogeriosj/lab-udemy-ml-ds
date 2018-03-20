import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as dates
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

sns.set_style("darkgrid")

def format_date(value):
    return datetime.strptime(value, '%Y%m%d-%H')


df = pd.read_csv('query_explorer.csv', delimiter='|')
df['datehour'] = df['date'].map(str) + '-' + df['hour'].map(str)
df['datetime'] = df['datehour'].apply(format_date)
del df['datehour']
del df['date']
del df['hour']
df.set_index(['datetime'], inplace=True)
print(df.tail())

fig, ax = plt.subplots()
ax.plot_date(df.index.to_pydatetime(), df['users'], 'b-')
ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(4,32, 4)))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
ax.xaxis.grid(True, which="minor")
ax.yaxis.grid()

ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
plt.tight_layout()
plt.show()

