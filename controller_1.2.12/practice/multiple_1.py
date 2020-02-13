import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pylab
import math
from displayfunction import display

from scipy import stats

import statsmodels.api as sm
from statsmodels.stats import diagnostic as diag
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error

df = pd.read_excel("/home/abzooba/Downloads/korea_data.xlsx")

df.replace("..","nan")


# set the index equal to year column
df.index = df['Year']
#print(df)

df = df.drop('Year', axis=1)
print(df)

# set the data type of each column to be float


#df = df.astype(float)
print(df.dtypes)

df = df.loc['1969' : '2016']
#print(df)

# rename column name
Column_name = { "GDP growth (annual %)" : "gdp_growth",
                "Gross capital formation (% of GDP)" : "gross_capital_formation",
                "Population growth (annual %)" : "pop_growth",
                "Birth rate, crude (per 1,000 people)" : "birth_rate",
                "Broad money growth (annual %)" : "broad_money_growth",
                "Final consumption expenditure (annual % growth)" : "final_consumption_expend",
                "General government final consumption expenditure (annual % growth)" : "general_govt_final_consp_grth",
                "Gross capital formation (annual % growth)" : "gross_capital_formation",
                "Households and NPISHs Final consumption expenditure (annual % growth)" : "household_final_consumption_exndtr",
                "Unemployment, total (% of total labor force) (national estimate)" : "Unemployment"

}

df = df.rename(columns = Column_name)
print(df)

# check for null
print(df.isnull().any())

print(df.head())

"""
df1=df.drop('V2',axis=1)
print(df.head())

#print(df.dtypes)

df2=df.astype(float)
#print(df2.dtypes)

df3 = df2.loc['0' : '25']
print(df3)

column_name = { "V1" : "Credit_rate",
                "V2" : "Debit_rate"
              }

# rename the Columns
df4 = df.rename(columns = column_name)
print(df4)

# check for null { if no null then it return False }
#display("-"*100)
#print(df.isnull().any())

print(df4.head())


corr = df.corr()
print(corr)
"""

