import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib
import numpy as np
import time

url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

names=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pd.read_csv(url,names=names)

print(df.head())
print(df.describe())

array=df.values
x=array[:,0:8]
y=array[:,8]
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.20,random_state=7)
#random state ensures that same train and test sets are created each time the code is run
model=LogisticRegression()
model.fit(x_train,y_train)
#time.sleep(10)
print("Model trained successfully")

#accuracy
result=model.score(x_test,y_test)
print("Accuracy: ",result)

#saving the model
filename='diabetic_model.pkl' #.sav format can be also used
joblib.dump(model,filename) 
print("Model saved successfully")
    
