#prediction
import numpy as np
import joblib
model=joblib.load('diabetic_model.pkl')
#x_test1=np.zeros((1,8))
x_test1=np.array([6,148,72,35,0,33.6,0.627,50]).reshape(1,-1)
#Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
k=0
#for i in names[0:8]:
    #x_test1[k]=eval(input(f"Enter {i}: "))
    #k=K+1
    
y_pred=model.predict(x_test1)
if y_pred==1:
    print("Predicted: Diabetic")
else: 
    print("Predicted: Not Diabetic")  