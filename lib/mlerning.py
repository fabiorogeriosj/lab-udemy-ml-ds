import numpy as np
import numbers

def calc1(n):
    return n * 2

def parse_file(f):
    data = np.genfromtxt(f, delimiter=',', usecols=(0,1,2,3))
    return data

def parse_csv(f):
    return np.genfromtxt(f, delimiter=";", skip_header=1)
