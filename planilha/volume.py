import pandas as pd

def csv(f):
    return pd.read_csv(f, delimiter=';')

def excel(f):
    return pd.read_excel(f)