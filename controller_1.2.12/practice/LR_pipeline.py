import numpy as np
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

X, y = load_boston(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

pipeline = Pipeline([('scaling', StandardScaler()),
                      ('regr',LinearRegression())])

model=pipeline.fit(X_train,y_train)

predictions=model.predict(X_test)

print('Prediction :',predictions[0:5])

print('y_test: ',y_test[0:5])

print('Model_score: ',model.score(X_test,y_test))





