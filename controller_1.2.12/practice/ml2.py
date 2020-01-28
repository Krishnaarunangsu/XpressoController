import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

path = "/home/abzooba/PycharmProjects/ReyazTest/python_practice/practice/data_num - Sheet1.csv"

features = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# reading the csv
data = pd.read_csv(path)

print(data.head())

print(data.shape)

print(data.describe())

print((data.groupby('Count')).size())

data.plot(kind='box', subplots=True, layout=(2, 2),
          sharex=False, sharey=False)

plt.show()

#data.hist()
#plt.show()

scatter_matrix(data)
plt.show()

print('-------------------------------------------------------------')
y = data['Count']
X = data.drop('Count', axis=1)
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.25, random_state=0)

print(X.head())
print('')
print(y.head())

algorithms = []
scores = []
names = []

algorithms.append(('Logisitic Regression', LogisticRegression()))
algorithms.append(('K-Nearest Neighbours', KNeighborsClassifier()))
algorithms.append(('Decision Tree Classifier', DecisionTreeClassifier()))

for name, algo in algorithms:
    k_fold = model_selection.KFold(n_splits=10, random_state=0)

    # Applying k-cross validation
    cvResults = model_selection.cross_val_score(algo, X_train, y_train,
                                                cv=k_fold, scoring='accuracy')

    scores.append(cvResults)
    names.append(name)
    print(str(name) + ' : ' + str(cvResults.mean()))

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(scores)
ax.set_xticklabels(names)
plt.show()

for name, algo in algorithms:
    clf = algo
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    pred_score = accuracy_score(y_test, y_pred)

    print(str(name) + ' : ' + str(pred_score))
    print('')
    print('Confusion Matrix: ' + str(confusion_matrix(y_test, y_pred)))
    print(classification_report(y_test, y_pred))






