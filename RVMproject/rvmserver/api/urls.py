from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.getAllusers),
    path('add/',views.addUser)
]
