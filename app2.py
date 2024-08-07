from flask import Flask,render_template,request
from asyncio import protocols
import pickle
import numpy as np
app=Flask(__name__)


@app.route('/') #decorator
def base():
    return render_template('home.html')
#['preg','plas','pres','skin','test','mass','pedi','age','class']
@app.route('/predict',methods=['post'])
def predict():
    model=pickle.load(open('diabetic_model.pkl','rb'))
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    
    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
    y_pred=model.predict(np.array([preg,plas,pres,skin,test,mass,pedi,age]).reshape(1,-1).astype(float))
    if y_pred[0]==1:
        data="Predicted: Diabetic"
    else: 
        data="Predicted: Not Diabetic"  
    return render_template('predict.html',data=data)
if __name__=="__main__":
    app.run(debug=True)