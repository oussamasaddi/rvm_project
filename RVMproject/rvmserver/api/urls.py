from django.urls import path 
from . import views 

from . import detectionsBottle 

urlpatterns = [
    path('',views.getAllusers),
    path('add/',views.addUser) , 
    path('detectbottle/', detectionsBottle.detectBottle)
]
