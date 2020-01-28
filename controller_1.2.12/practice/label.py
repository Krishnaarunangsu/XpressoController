import pandas as pd

df = pd.read_csv("/home/abzooba/Downloads/ordinal_data.csv")
print(df)
print(df.dtypes)

print('-------------------------------------')
df["Feedback"] = df["Feedback"].astype('category')
print(df.dtypes)

print('-------------------------------------')

df["Feedback_cat"] = df["Feedback"].cat.codes
print(df)

