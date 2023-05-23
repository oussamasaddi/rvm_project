from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from django.http import HttpResponseBadRequest
from xml.etree import ElementTree
import json

import cv2
import face_recognition
import os
import numpy as np

from PIL import Image
import base64
import io

from . import firebaseconfig

database = firebaseconfig.database()




@api_view(['POST'])
def face_recognition_api(request):
  
  encoded_image = eval(request.data["image"].encode('utf-8'))
 
  decoded_image = base64.b64decode(encoded_image)
  
  person_name = "unknown"  
  try:
    image = Image.open(io.BytesIO(decoded_image))
    cv2image = convert_image_cv2(image)
    person_name = rec_fac(cv2image)
    #image.save("ehhe.png")
  except Exception as e:
        return HttpResponseBadRequest("Invalid image: {}".format(str(e)))

  
  return Response(person_name)








def rec_fac(imgg):

    pict,nnm = read_image()


      # Load a second image and detect faces
    image2 = imgg
    image2 = cv2.resize(image2, (180, 180))

    rgb2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    boxes2 = face_recognition.face_locations(rgb2, model='hog')

    bb  = 0
    namefound="unknown"

    for image in pict :
          # Load an image and detect faces
        
        image = cv2.resize(image, (180, 180))

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model='hog')
        

        # Loop over each face and encode it
        encodings = []
        for box in boxes:
            top, right, bottom, left = box
            face = rgb[top:bottom, left:right]
            encoding = face_recognition.face_encodings(image)[0]
            encodings.append(encoding)

        

        # Loop over each face in the second image and compare to the known faces
        for box in boxes2:
            top, right, bottom, left = box
            face = rgb2[top:bottom, left:right]
            encoding = face_recognition.face_encodings(image2)[0]
            matches = face_recognition.compare_faces(encodings, encoding , tolerance=0.5)
            name = "Unknown"

            # If there's a match, assign the name of the person
            if matches[0]:
              namefound=nnm[bb]
              print(bb)
              print(matches)
        
        
              
              
        bb=bb + 1
    name = namefound
        # Draw a rectangle around the face and label it
    return name


def read_image():
    dir_path = "C:/Users/oussa/django_projects/rvm_project/RVMproject/rvmserver/api/picfo"
    imagedata=[]
    imagename=[]

# loop over files in directory
    for filename in os.listdir(dir_path):
        # check if file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # read image using cv2.imread()
            img = cv2.imread(os.path.join(dir_path, filename))
            imagedata.append(img)
            imagename.append(filename.split(".")[0])
    
    return imagedata , imagename


def convert_image_cv2(pil_image):
    # convert PIL image to numpy array
    numpy_image = np.array(pil_image)

    # convert numpy array to cv2 image
    cv2_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
    return cv2_image
            