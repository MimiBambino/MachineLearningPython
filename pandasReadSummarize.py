__author__ = 'cynthia_odonnell'
import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

# target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
# "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
# #read rocks versus mines data into pandas data frame
# rocksVMines = pd.read_csv(target_url,header=None, prefix="V")
# #print head and tail of data frame
# print(rocksVMines.head())
# print(rocksVMines.tail())
# #print summary of data frame
# summary = rocksVMines.describe()
# print(summary)

target_url = ("http://archive.ics.uci.edu/ml/machine-"
"learning-databases/wine-quality/winequality-red.csv")
wine = pd.read_csv(target_url,header=0, sep=";")
print(wine.head())
#generate statistical summaries
summary = wine.describe()
print(summary)
wineNormalized = wine
ncols = len(wineNormalized.columns)
for i in range(ncols):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
wineNormalized.iloc[:,i:(i + 1)] = (wineNormalized.iloc[:,i:(i + 1)] - mean) / sd
array = wineNormalized.values
boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized "))
show()