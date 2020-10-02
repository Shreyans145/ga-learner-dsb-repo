# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


# store the dataframe
df = pd.read_csv(path)

# store independent variable
X = df.drop('insuranceclaim',axis=1)

# store dependent variable
y = df['insuranceclaim']

# spliting the dataset
X_train,X_test,y_train,y_test=train_test_split(X,y ,test_size=0.2,random_state=6)
# code ends here


# --------------
import matplotlib.pyplot as plt


# Code starts here
q_value = X_train['bmi'].quantile(0.95)
plt.boxplot(X_train['bmi'], notch=None, vert=None, patch_artist=None, widths=None)
y_train.value_counts(normalize=True)

# Code ends here


# --------------
# Code starts here
relation = X_train.corr()

print(relation)
sns.pairplot(X_train)

# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here
cols = ['children','sex','region','smoker']
fig, axes = plt.subplots(2, 2)
for i in range(0,2):
    for j in range(0,2):
        col = cols[ i * 2 + j]
sns.countplot(x=X_train[col], hue=y_train, ax=axes[i,j])
# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here

# instantiate logistic regression model
lr=LogisticRegression(random_state=9)
# grid search on logistic regression

grid = GridSearchCV(estimator=lr, param_grid=parameters)
grid.fit(X_train, y_train)

# make predictions 
y_pred = grid.predict(X_test)
accuracy= accuracy_score(y_pred,y_test)

print(accuracy)



# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here
score = roc_auc_score( y_test, y_pred)
print(score)
y_pred_proba = grid.predict_proba(X_test)[:,1]
print(y_pred_proba[0])
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(roc_auc)
plt.plot(fpr,tpr,label="Logistic model, auc="+str(roc_auc))
plt.legend(loc=4)
plt.show()
# Code ends here
print(round(score,2))
print(round(y_pred_proba[0],2))
print(round(roc_auc,2))


