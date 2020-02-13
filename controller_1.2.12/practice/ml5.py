import pandas as pd

path = "/home/abzooba/PycharmProjects/ReyazTest/python_practice/practice/data_num - Sheet1.csv"

#features = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# reading the csv
data = pd.read_csv(path)

print(data.head())

print(data.shape)

print(data.describe())


