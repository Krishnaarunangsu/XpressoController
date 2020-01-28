import pandas as pd
import numpy as np

df = pd.read_csv("/home/abzooba/Downloads/ordinal_data.csv")
print(df.head())
print(df.dtypes)

print('*******************************')
print("Number of different values in column Feedback :")
print(df["Feedback"].value_counts())

print("---------------------------------")
ord = pd.get_dummies(df, columns=["Feedback"]).head()
print(ord)


