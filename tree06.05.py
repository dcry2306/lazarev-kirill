from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import GridSearchCV 
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

parameters = {'criterion': ['gini', 'entropy'],
              'max_depth': [1,2],
              'min_samples_split': [2, 5, 10]}

dt = DecisionTreeClassifier()

gridsearch = GridSearchCV(dt, parameters, cv=5)
gridsearch.fit(X_train, y_train)

best_params = gridsearch.best_params_
print('Наилучшие параметры: ', best_params)

dt = DecisionTreeClassifier(criterion='gini', max_depth= 2, min_samples_split=2)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Оценка accuracy на тестовом наборе: ', accuracy)