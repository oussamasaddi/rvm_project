from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
import os 
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from PIL import Image
import requests
from io import BytesIO



from ultralytics import YOLO

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


#model rvm 

model_cannete_path = os.path.abspath('canetmodel.pt')
modelcannet = YOLO(model_cannete_path)

model_bottle_path = os.path.abspath('modelbottle.pt')
modelbottle = YOLO(model_bottle_path)

odel_bottle_can_path = os.path.abspath('can_bot.pt')
modelBottleCan = YOLO(odel_bottle_can_path)

@api_view(['POST'])
def model_rvm(request):
  rslt = {"Type":"UNKNOWN" , "Result":"DENY"}
  labels_canette = ["CANNETTE","CANNETTE_DEFORME"]
  labels_bottle = ["BOUCHON","BOUTEILLE ","BOUTEILLE_DEFORMEE","BOUTEILLE_DEFORMEE"]
  labels_bottle_canete = ["BOUCHON","BOUTEILLE ","BOUTEILLE","CANNETTE","CANNETTE"]
  response = requests.get("https://pbs.twimg.com/media/Es-ocp-XUAAiAZv.jpg:large")
  image = Image.open(BytesIO(response.content))
 #image = Image.open("/content/datasets/nisi-5/valid/images/02_03_2020_14_33_36-Copie-Copie-Copie_jpeg.rf.5e05ba2f22d5f5b9e7adcf3b0e0f9fa2.jpg")
  #image=image.resize((224,224))
  image = np.asarray(image)
  resultsBC = modelBottleCan.predict(image)
  labelBC = labels_bottle_canete[int(resultsBC[0].boxes.boxes[0][-1])]
  print("hhhhh" , resultsBC[0].boxes.boxes[0][-2] > 0.5 , labelBC)
  if((resultsBC[0].boxes.boxes[0][-2] > 0,5) and (labelBC == 'BOUTEILLE') ):
    resultsB = modelbottle.predict(image)
    labelB = labels_bottle[int(resultsB[0].boxes.boxes[0][-1])]
    if((resultsB[0].boxes.boxes[0][-2] > 0,5) and (labelB == 'BOUTEILLE') ):
      rslt = {"Type":"BOUTEILLE" , "Result":"ACCEPTE"}

      return  Response(rslt)
    else : 
      rslt = {"Type":"BOUTEILLE_DEFORME" , "Result":"DENY"}
      return  Response(rslt)
  elif ((resultsBC[0].boxes.boxes[0][-2] > 0,5) and (labelBC == 'CANNETTE') ):
    resultsC = modelcannet.predict(image)
    labelC = labels_canette[int(resultsC[0].boxes.boxes[0][-1])]
    if((resultsC[0].boxes.boxes[0][-2] >= 0,5) and ( labelC == 'CANNETTE') ):
      rslt = {"Type":"CANNETTE" , "Result":"ACCEPTE"}
      return  Response(rslt)
    else : 
      rslt = {"Type":"CANNETTE_DEFORME" , "Result":"DENY"}
      return  Response(rslt)
  elif((resultsBC[0].boxes.boxes[0][-2] > 0,5) and (labelBC == 'BOUCHON') ):
      rslt = {"Type":"BOUCHON" , "Result":"DENY"}
      return  Response(rslt)

  else:
    return  Response(rslt)









  



