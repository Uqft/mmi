import numpy as np
import pandas as pd 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import tree

df = pd.read_csv('metric.csv')
x = df.iloc[:,:3]
y = df.iloc[:,3:]

model=tree.DecisionTreeClassifier(criterion="entropy")
model.fit(x,y)

x, x_validation, y, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)
predictions = model.predict(x_validation)

print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))

print (model.predict([[1,1,1]]))
