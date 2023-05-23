from . import firebaseconfig
from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
import joblib
database = firebaseconfig.database()
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
model_path1 = os.path.abspath('sarima.joblib')

model_sarima = joblib.load(model_path1)

@api_view(['POST'])
def model1(request):
 i = request.data["steps"]
 predictsd = model_sarima.forecast(steps=i)
 p = int(predictsd.sum())
 return Response({'result': p})



model_path2 = os.path.abspath('arima_model.joblib')
model_arima = joblib.load(model_path2)
# Load the saved machine learning model


@api_view(['POST'])
def model2(request):
 i = request.data["steps"]
 predictsd = model_arima.forecast(steps=i)
 p = int(predictsd.sum())
  
 return Response(p)


model_path3 = os.path.abspath('wiem_model.joblib')
model_wiem = joblib.load(model_path3)

@api_view(['POST'])
def model_w(request):  
    
  age = request.data["education"]
  workclass = request.data["education-num"]
  education = request.data["marital-status"]
  marital_status = request.data["occupation"]
  occupation = request.data["sex"]
  race = request.data["hours-per-week"]
  country = request.data["native-country"]
  income = request.data["AgeRange"]

  dfd  = [[	age	,workclass, education ,	marital_status,	occupation ,	race	,	country,	income	]]
  dfd = pd.DataFrame(dfd)
  dfd.columns = ["education",	"education-num",	"marital-status","occupation",	"sex",	"hours-per-week",	"native-country",	"AgeRange"]
  

  categorical_cols = ['education','marital-status','occupation','sex','native-country','AgeRange']
  dfd[categorical_cols] = dfd[categorical_cols].apply(lambda x: pd.factorize(x)[0]) # convert categorical columns to numerical labels

  #scaler = MinMaxScaler()
  #dfd = pd.DataFrame(scaler.fit_transform(dfd), columns=dfd.columns)
  #************************
  #tt  = [[	0.561644	,0.000,	0.066667,	0.333333,	0.500000,	0.25	,1.0,	0.397959,	0.0,	0.0	]]
  #fg = pd.DataFrame(tt)
  #fg.columns = ["age",	"workclass",	"education",	"marital-status",	"occupation",	"race",	"sex",	"hours-per-week",	"native-country",	"income"]
  #pr = mhiri.predict(tt)
  
  a = model_wiem.predict(dfd)
  print(a)
  succ = {"fidele" : a[0]}
  return Response(succ)
    
    
model_path4 = os.path.abspath('arimamohannad.joblib')

model_haned = joblib.load(model_path4)

@api_view(['POST'])
def model3(request):
 i = request.data["steps"]
 predictsd = model_haned.forecast(steps=i)
 p = int(predictsd.sum())
 return Response({'result': p})