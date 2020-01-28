from pandas import read_csv

path = "/home/abzooba/PycharmProjects/ReyazTest/python_practice/practice/Travel Expenses - Sheet1.csv"
data = read_csv(path)
print(data.shape)
print(data[:3])

print(data.head(5))
print(data.dtypes)

print(data.describe())

count_Expen = data.groupby('City').size()
print(count_Expen)

correlations = data.corr(method='pearson')
print(correlations)
print('Skew \n',data.skew())


