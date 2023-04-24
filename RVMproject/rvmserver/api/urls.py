from django.urls import path 
from . import views 

from . import detectionsBottle 
from . import detectionuser 


urlpatterns = [
    path('',views.getAllusers),
    path('add/',views.addUser) , 
    path('detectbottle/', detectionsBottle.detectBottle),
    path('facedetection/',detectionuser.face_recognition_api )
]
