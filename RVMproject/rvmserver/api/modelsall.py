from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
import os 
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

model_path = os.path.abspath('mhiri.joblib')

modelmhiri = joblib.load(model_path)



@api_view(['POST'])
def predmhiri(request):
  age = request.data["age"]
  workclass = request.data["workclass"]
  education = request.data["education"]
  marital_status = request.data["maritalstatus"]
  occupation = request.data["occupation"]
  race = request.data["race"]
  hours = request.data["hours"]
  country = request.data["country"]
  income = request.data["income"]
  sex = request.data["sex"]
  dfd  = [[	age	,workclass, education ,	marital_status,	occupation ,	race	,sex,	hours,	country,	income	]]
  dfd = pd.DataFrame(dfd)
  dfd.columns = ["age",	"workclass",	"education",	"marital-status",	"occupation",	"race",	"sex",	"hours-per-week",	"native-country",	"income"]
  

  dfd['income'] = dfd['income'].map({'<=50K': 0, '>50K': 1})
  categorical_cols = ['workclass','education','marital-status','occupation','race','sex','native-country']
  dfd[categorical_cols] = dfd[categorical_cols].apply(lambda x: pd.factorize(x)[0]) # convert categorical columns to numerical labels

  scaler = MinMaxScaler()
  dfd = pd.DataFrame(scaler.fit_transform(dfd), columns=dfd.columns)



  #************************
  #tt  = [[	0.561644	,0.000,	0.066667,	0.333333,	0.500000,	0.25	,1.0,	0.397959,	0.0,	0.0	]]
  #fg = pd.DataFrame(tt)
  #fg.columns = ["age",	"workclass",	"education",	"marital-status",	"occupation",	"race",	"sex",	"hours-per-week",	"native-country",	"income"]
  #pr = mhiri.predict(tt)
  
  a = modelmhiri.predict(dfd)
  succ = {"success" : a[0]}
  return Response(succ)