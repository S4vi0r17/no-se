import pandas as pd
import numpy as np
import matplotlib.pylab as plt

plt.ion()  # Enables interactive mode for matplotlib
plt.style.use('seaborn-v0_8-whitegrid')
plt.rc('text', usetex=True)
plt.rc('font', family='times')
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('font', size=12)

ruta = 'educ_figdp_1_Data.csv'
edu = pd.read_csv(ruta, na_values=':', usecols=['TIME', 'GEO', 'Value'])
print(edu.head())

print()
print('edu.columns')
print(edu.columns)

print()
print('edu.index')
print(edu.index)

print()
print('edu.dtypes')
print(edu.values)
