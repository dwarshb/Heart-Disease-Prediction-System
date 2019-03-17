


import main
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
data=pd.read_csv('F:\darshan\datasets\heart-attack-prediction\data.csv',names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "exang", "num"]);
for column in data.columns:
    if data[column].dtype == type(object):
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
X = data.drop('age',axis=1)
y = data['num']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train.astype(float))
StandardScaler(copy=True, with_mean=True, with_std=True)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train.astype(float))
X_test = scaler.transform(X_test.astype(float))
print(X_test)

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier

ann_clf = MLPClassifier()
parameters = {'solver': ['lbfgs'],
              'alpha': [1e-4],
              'hidden_layer_sizes':(8,50,50,2),
              'random_state':[1]}

acc_scorer = make_scorer(accuracy_score)
grid_obj = GridSearchCV(ann_clf,parameters,scoring=acc_scorer)
grid_onj = grid_obj.fit(X_train,y_train)
ann_clf = grid_obj.best_estimator_
ann_clf.fit(X_train,y_train)
y_pred_ann = ann_clf.predict(X_test)
def prediction(age,sex,cp,bp,cholesterol,blood_sugar,heart_rate,exercise):
    print(age,sex,cp,bp,cholesterol,blood_sugar,heart_rate,exercise)
    val = ann_clf.predict([[age,sex,cp,bp,cholesterol,blood_sugar,heart_rate,exercise]])    
    #val = ann_clf.predict([[66,1,2,190,263,320,173,0]])
    print(val)
    from sklearn.metrics import confusion_matrix
    cm_ann = confusion_matrix(y_test,y_pred_ann)
    print(cm_ann)
    ann_result = accuracy_score(y_test,y_pred_ann)
    print(ann_result)
    return val
