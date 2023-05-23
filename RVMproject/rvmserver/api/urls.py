from django.urls import path 
from . import views 

from . import detectionsBottle 
from . import detectionuser 
from . import modelsall 
from . import machine 
from . import bottles 

from . import Models


urlpatterns = [
    path('',views.getAllusers),
    path('add/',views.addUser) , 
    path('detectbottle/', detectionsBottle.detectBottle),
    path('facedetection/',detectionuser.face_recognition_api ),
    path('mhiri/',modelsall.predmhiri ),
    path('rvmmodel/',modelsall.model_rvm ),
    path('getAllmachines/',machine.getAllmachines),
    path('addmachine/',machine.addMachine),
    path('<str:id>/deleteMachine/',machine.deleteMachine),
    path('<str:id>/updateMachine/',machine.updateMachine),
    path('searchM/', machine.searchMachines),
    path('deleteAllMachines/', machine.deleteAllMachines),
    path('addbottles/', bottles.addbottles),
    path('getAllbottles/', bottles.getAllbottles),
    path('<str:id>/deletebottle/',bottles.deletebottle),
    path('<str:id>/updateBottle/',bottles.updateBottle),
    path('search_B/',bottles.searchbottles),
    path('deleteAllbottles/', bottles.deleteAllMachines),
    path('model1/', Models.model1, name='predict_1**'),
    path('model2/', Models.model2, name='predict_2'),
    path('model_wiem/', Models.model_w, name='predict_w'),
    path('model_hanned/', Models.model3, name='predict_h')

]
