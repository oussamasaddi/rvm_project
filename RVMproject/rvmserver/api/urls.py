from django.urls import path 
from . import views 

from . import detectionsBottle 
from . import detectionuser 
from . import modelsall 



urlpatterns = [
    path('',views.getAllusers),
    path('add/',views.addUser) , 
    path('detectbottle/', detectionsBottle.detectBottle),
    path('facedetection/',detectionuser.face_recognition_api ),
    path('mhiri/',modelsall.predmhiri ),
    path('rvmmodel/',modelsall.model_rvm )

]
