import pandas as pd
import numpy as np

df1=pd.read_csv('/home/abzooba/PycharmProjects/ReyazTest/python_practice/practice/Travel Expenses - Sheet1.csv')

print(df1)

print(df1.aggregate({'Expenses':['sum','min', 'max']}))
print('Avg',df1['Expenses'].mean())

#print('Sum',df1['Expenses'].sum())

print(df1.sort_values('Expenses'))
print('***********************')
print(df1.sort_values('Expenses',ascending=False))

print('----------------------------------')


grp1 = df1.groupby('City')

print(grp1.get_group('Kolkata'))
print('***********************')

print(grp1.get_group('Chennai'))
print('***********************')

print(grp1.get_group('Delhi'))
print('***********************')

print(grp1.aggregate({'Expenses':['sum', 'min' ,'max']}))
print('Avg',grp1['Expenses'].mean())






