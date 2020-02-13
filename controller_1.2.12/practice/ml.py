import csv
import numpy as np
from pandas import set_option
import pandas as pd
from pandas import read_csv

path = r"/home/abzooba/PycharmProjects/ReyazTest/python_practice/practice/data_num - Sheet1.csv"

with open(path,'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = list(reader)
    data = np.array(data).astype(int)

print(headers)
print(data.shape)
print(data[:10])

set_option('display.width', 100)
set_option('precision', 2)


print(data.dtype)
print(data.describe())

'''
correlations = data.corr(method='pearson')
print(correlations)

data = read_csv(path)
print(data.shape)
print(data[:3])
'''