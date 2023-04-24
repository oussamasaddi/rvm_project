from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from django.http import HttpResponseBadRequest
from xml.etree import ElementTree
import json


from PIL import Image
import base64
import io

from . import firebaseconfig

database = firebaseconfig.database()




@api_view(['POST'])
def detectBottle(request):
  
  encoded_image = eval(request.data["image"].encode('utf-8'))
 
  decoded_image = base64.b64decode(encoded_image)
  

  try:
    image = Image.open(io.BytesIO(decoded_image))
    
    #image.save("ehhe.png")
  except Exception as e:
        return HttpResponseBadRequest("Invalid image: {}".format(str(e)))

  
  

  
  

  
  return Response("yy")