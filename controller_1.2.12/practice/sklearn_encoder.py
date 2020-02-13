import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/home/abzooba/Downloads/ordinal_data.csv")
print(df)
print(df.dtypes)

print('-------------------------------------')


lb_make = LabelEncoder()
df["Feedback_cat"] = lb_make.fit_transform(df["Feedback"])
#print(df[["Feedback", "Feedback_cat"]].head())
print(df)


